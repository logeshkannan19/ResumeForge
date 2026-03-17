from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from app.services.parser import FileParser
from app.services.ai_service import AIService
from app.utils.database import get_database
from app.auth.security import oauth2_scheme
from jose import jwt, JWTError
from app.auth.security import SECRET_KEY, ALGORITHM
from bson import ObjectId
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

async def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    """Validate JWT token and return the user's email."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return email
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...), current_user: str = Depends(get_current_user)):
    """
    Handle resume upload, parsing, and storage.
    
    Args:
        file (UploadFile): The PDF or DOCX file.
        current_user (str): Email of the authenticated user.
        
    Returns:
        dict: The ID of the stored resume document.
    """
    content = await file.read()
    try:
        text = FileParser.parse_file(content, file.filename)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    db = await get_database()
    resume_doc = {
        "user_email": current_user,
        "filename": file.filename,
        "raw_text": text,
        "analysis": None
    }
    try:
        result = await db.resumes.insert_one(resume_doc)
        return {"id": str(result.inserted_id), "message": "Resume uploaded and text extracted."}
    except Exception as e:
        logger.error(f"Failed to save resume: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal database error.")

@router.post("/analyze-resume/{resume_id}")
async def analyze_resume(resume_id: str, current_user: str = Depends(get_current_user)):
    """
    Initiate AI analysis for a specific resume.
    """
    db = await get_database()
    resume = await db.resumes.find_one({"_id": ObjectId(resume_id), "user_email": current_user})
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found or access denied.")
    
    analysis = await AIService.analyze_resume(resume["raw_text"])
    await db.resumes.update_one({"_id": ObjectId(resume_id)}, {"$set": {"analysis": analysis}})
    return analysis

@router.post("/match-job")
async def match_job(resume_id: str, job_description: str, current_user: str = Depends(get_current_user)):
    """
    Match a stored resume against a provided job description.
    """
    db = await get_database()
    resume = await db.resumes.find_one({"_id": ObjectId(resume_id), "user_email": current_user})
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found.")
    
    match_result = await AIService.match_job(resume["raw_text"], job_description)
    return match_result

@router.get("/resumes")
async def get_resumes(current_user: str = Depends(get_current_user)):
    """
    List all resumes for the current authenticated user.
    """
    db = await get_database()
    resumes_list = await db.resumes.find({"user_email": current_user}).to_list(100)
    for r in resumes_list:
        r["_id"] = str(r["_id"])
    return resumes_list
