# ⚒️ ResumeForge

[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)](https://python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

> [!NOTE]
> **Live Demo:** [resumeforge-landing.vercel.app](https://resumeforge-landing.vercel.app)

Stop shouting into the void. Build a resume that actually gets read.

ResumeForge is an AI-powered resume builder that analyzes your experience through the eyes of a recruiter. It spots gaps, suggests impact verbs, and helps you align perfectly with jobs.

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 **AI ATS Analysis** | Score your resume like modern hiring systems do |
| 🎯 **Job Matching** | Paste job description and tailor your content |
| 📝 **Smart Builder** | Generate clean, professional PDFs |
| 🔒 **Privacy First** | JWT auth + secure password hashing |

## 🛠 Tech Stack

| Component | Technology |
|----------|------------|
| **Backend** | FastAPI |
| **Database** | MongoDB |
| **AI** | OpenAI GPT-3.5/4 |
| **PDF** | ReportLab |
| **Frontend** | HTML/CSS + Vanilla JS |

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/logeshkannan19/ResumeForge.git
cd ResumeForge

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Add your OPENAI_API_KEY

# Seed database (optional)
python -m scripts.seed_db

# Start server
uvicorn app.main:app --reload
```

Visit `http://localhost:8000`

## 📁 Project Structure

```
ResumeForge/
├── app/
│   ├── main.py          # FastAPI app
│   ├── auth/            # Authentication
│   ├── models/          # Database models
│   ├── routes/          # API routes
│   ├── services/        # Business logic
│   └── utils/           # Utilities
├── scripts/
│   └── seed_db.py       # Database seeder
├── templates/            # HTML templates
├── static/              # CSS/JS assets
├── uploads/             # File uploads
└── requirements.txt
```

## 🔑 Environment Variables

| Variable | Description |
|----------|-------------|
| `OPENAI_API_KEY` | OpenAI API key for GPT |
| `MONGODB_URI` | MongoDB connection string |
| `JWT_SECRET` | JWT token secret |
| `PORT` | Server port |

## 🤝 Contributing

Contributions welcome! Please [open an issue](https://github.com/logeshkannan19/ResumeForge/issues) for bugs or features.

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.
