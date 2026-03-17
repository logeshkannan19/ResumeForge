import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

# We use this script to quickly get a local environment up and running.
# It populates the DB with a test user and some sample resumes so you don't have to 
# manually upload files just to see the dashboard in action.

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "resumeforge")

async def seed():
    print(f"Connecting to {DATABASE_NAME} at {MONGODB_URL}...")
    client = AsyncIOMotorClient(MONGODB_URL)
    db = client[DATABASE_NAME]

    # Clear existing data - use with caution!
    # print("Cleaning up old data...")
    # await db.users.delete_many({})
    # await db.resumes.delete_many({})

    print("Seeding sample data...")
    
    # Mock user - password is 'password123' (hashed version)
    mock_user = {
        "email": "dev@resumeforge.ai",
        "full_name": "Dev User",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6L6s57gzRT0.7uwi" 
    }
    
    await db.users.update_one({"email": mock_user["email"]}, {"$set": mock_user}, upsert=True)

    mock_resume = {
        "user_email": "dev@resumeforge.ai",
        "filename": "sample_resume.pdf",
        "raw_text": "Experienced Python Developer with a passion for building clean, human-centric applications. Expert in FastAPI and MongoDB.",
        "analysis": {
            "ats_score": 85,
            "skills": ["Python", "FastAPI", "MongoDB", "Asyncio"],
            "missing_keywords": ["Docker", "Kubernetes"],
            "strengths": ["Strong backend experience", "Clean code practices"],
            "weaknesses": ["Minor gaps in DevOps tooling"],
            "suggestions": ["Add more details on cloud-native deployments."]
        }
    }
    
    await db.resumes.insert_one(mock_resume)
    
    print("Done! You can now log in with 'dev@resumeforge.ai' and 'password123'.")

if __name__ == "__main__":
    asyncio.run(seed())
