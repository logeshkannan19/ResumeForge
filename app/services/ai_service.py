import openai
import os
from dotenv import load_dotenv
import json

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class AIService:
    @staticmethod
    async def analyze_resume(resume_text: str):
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
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)

    @staticmethod
    async def match_job(resume_text: str, job_description: str):
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
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)
