# ARCHITECTURE.md - ResumeForge

## Technical Overview

ResumeForge is built with a decoupled architecture, separating the FastAPI backend from the static frontend. It leverages asynchronous processing for database interactions and AI analysis.

## Core Components

### 1. Backend (FastAPI)
- **API Layer**: Handles HTTP requests, validation, and routing.
- **Service Layer**: Encapsulates business logic, including AI analysis (OpenAI) and file parsing.
- **Data Layer**: Asynchronous MongoDB interaction using Motor.
- **Auth Layer**: JWT-based security system.

### 2. Frontend (Vanilla JS + CSS)
- **Single Page Architecture**: Managed through basic routing and dynamic DOM updates.
- **Design System**: Responsive CSS with glassmorphism and modern styling.

## Data Flow

1. **Upload**: User uploads PDF/DOCX -> FastAPI parses text -> Stores raw text in MongoDB.
2. **Analysis**: User requests analysis -> AI Service calls OpenAI -> Stores JSON results -> Returns to UI.
3. **Builder**: User fills form -> FastAPI generates PDF via ReportLab -> Returns downloadable file.

## AI Integration

We use OpenAI's GPT-3.5 Turbo model with structured JSON output for:
- ATS Scoring
- Skill Extraction
- Improving Bullet Points
- Job Matching
