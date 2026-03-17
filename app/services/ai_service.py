import openai
import os
from dotenv import load_dotenv
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class AIService:
    """Service for interacting with OpenAI to analyze and improve resumes."""

    @staticmethod
    async def analyze_resume(resume_text: str):
        """
        Analyze resume text using OpenAI GPT-3.5 API.
        
        Args:
            resume_text (str): The raw text extracted from the resume.
            
        Returns:
            dict: Analysis results containing ATS score, skills, strengths, etc.
        """
        prompt = f"""
        Analyze the following resume text and provide:
        1. ATS Score (0-100)
        2. Key Skills identified
        3. Missing Keywords
        4. Strengths
        5. Weaknesses
        6. Suggestions for improvement

        Resume Text:
        {resume_text}

        Return the result in JSON format with the following keys:
        'ats_score', 'skills', 'missing_keywords', 'strengths', 'weaknesses', 'suggestions'.
        """
        try:
            response = await openai.ChatCompletion.acreate(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"}
            )
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            logger.error(f"Error during AI analysis: {str(e)}")
            return {
                "ats_score": 0,
                "skills": [],
                "missing_keywords": [],
                "strengths": ["Analysis failed. Please try again later."],
                "weaknesses": [],
                "suggestions": []
            }

    @staticmethod
    async def match_job(resume_text: str, job_description: str):
        """
        Match resume against a job description.

        Args:
            resume_text (str): Raw resume text.
            job_description (str): Target job description.

        Returns:
            dict: Match score and skill gap analysis.
        """
        prompt = f"""
        Compare the following resume with the job description:
        
        Resume: {resume_text}
        Job Description: {job_description}

        Provide:
        1. Match Score (%)
        2. Highlighted Missing Skills
        3. Fit analysis

        Return the result in JSON format with the following keys:
        'match_score', 'missing_skills', 'fit_analysis'.
        """
        try:
            response = await openai.ChatCompletion.acreate(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"}
            )
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            logger.error(f"Error during job matching: {str(e)}")
            return {
                "match_score": 0,
                "missing_skills": [],
                "fit_analysis": "An error occurred during matching."
            }
