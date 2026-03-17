from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.auth.security import create_access_token, verify_password, get_password_hash
from app.models.schemas import UserCreate, Token
from app.utils.database import get_database
import logging

logger = logging.getLogger(__name__)
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_user(email: str):
    """Retrieve a user from the database by email."""
    db = await get_database()
    return await db.users.find_one({"email": email})

@router.post("/register", response_model=Token)
async def register(user: UserCreate):
    """
    Register a new user and return an access token.
    
    Args:
        user (UserCreate): The user registration data.
        
    Returns:
        dict: The access token and token type.
    """
    db = await get_database()
    existing_user = await get_user(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user.password)
    user_dict = user.dict()
    user_dict.pop("password")
    user_dict["hashed_password"] = hashed_password
    
    try:
        await db.users.insert_one(user_dict)
    except Exception as e:
        logger.error(f"Failed to register user: {str(e)}")
        raise HTTPException(status_code=500, detail="Database error during registration")
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Authenticate a user and return an access token.
    
    Args:
        form_data (OAuth2PasswordRequestForm): Login credentials (email/password).
        
    Returns:
        dict: The access token and token type.
    """
    user = await get_user(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}
