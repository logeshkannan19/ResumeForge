# ResumeForge AI Resume Analyzer & Builder

Forge a resume that gets you hired. This project uses FastAPI, MongoDB, and OpenAI to provide AI-powered resume analysis, improvement suggestions, and a professional resume builder.

## 🚀 Features

- **AI Resume Analysis**: Get an ATS score, identify missing keywords, and see strengths/weaknesses.
- **Job Matching**: Compare your resume against specific job descriptions.
- **Resume Builder**: Create a professional resume from scratch and export as PDF.
- **Secure Auth**: JWT-based authentication with bcrypt password hashing.
- **Premium UI**: Modern glassmorphism design with dark mode.

## 🛠️ Tech Stack

- **Backend**: FastAPI, Uvicorn, Motor (Async MongoDB)
- **AI**: OpenAI GPT-3.5 API
- **Parsing**: pdfplumber, python-docx
- **PDF Generation**: ReportLab
- **Frontend**: Vanilla HTML5, CSS3 (Glassmorphism), JavaScript

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd resumeforge
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure Environment Variables:
   Create a `.env` file based on `.env.example`:
   ```env
   MONGODB_URL=mongodb://localhost:27017
   DATABASE_NAME=resumeforge
   SECRET_KEY=your_secret_key
   OPENAI_API_KEY=your_openai_api_key
   ```

4. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## 📂 Project Structure

```
resumeforge/
├── app/
│   ├── auth/          # JWT Security
│   ├── models/        # Schemas
│   ├── routes/        # API Endpoints
│   ├── services/      # AI & Parsing
│   ├── utils/         # Helpers
│   └── main.py        # Entry Point
├── static/            # CSS & JS
├── templates/         # HTML Files
└── uploads/           # File Storage
```
