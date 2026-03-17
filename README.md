# ⚒️ ResumeForge

### Stop shouting into the void. Build a resume that actually gets read.

We've all been there: spending hours tweaking a bullet point, only to have our application swallowed by a "black box" Applicant Tracking System (ATS). We built **ResumeForge** to give you the keys to that box.

ResumeForge isn't just another resume builder. It’s an AI-powered partner that looks at your experience through the eyes of a recruiter. It spots the gaps, suggests the impact verbs you’re missing, and helps you align perfectly with the jobs you actually want.

---

## ✨ Features that actually matter

- **ATS-Eye View**: Our AI analyzes your resume exactly like a modern hiring system does. Get a score and a list of "must-have" keywords you're missing.
- **The Matchmaker**: Paste a job description and literally watch the gaps disappear as we help you tailor your content.
- **Craft, Don't Just Type**: Use our built-in builder to generate a clean, professional PDF that doesn't look like a template from 2005.
- **Privacy by Design**: Your data is yours. We use secure JWT auth and industry-standard hashing to keep your career history safe.

## 🛠️ The Tech Under the Hood

We kept it lean and fast:
- **FastAPI**: For a snappy, asynchronous backend.
- **Motor & MongoDB**: Because your resume data is document-based, and we love the flexibility of a NoSQL schema.
- **OpenAI GPT-3.5**: The brains. We’ve tuned the prompts to focus on *action* and *impact*, not just generic fluff.
- **ReportLab**: Precise PDF generation because details matter.
- **Vanilla CSS (Glassmorphism)**: A modern, premium UI that feels fast and looks stunning.

## 🚀 Get Running in 5 Minutes

1. **Clone & Enter**:
   ```bash
   git clone https://github.com/logeshkannan19/ResumeForge.git
   cd resumeforge
   ```

2. **Fuel Up**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Secrets & Keys**:
   Copy `.env.example` to `.env` and add your `OPENAI_API_KEY`.

4. **Seed the Forge (Developer Utility)**:
   We built a script to help you see the dashboard immediately without uploading anything:
   ```bash
   python -m scripts.seed_db
   ```

5. **Let's Go**:
   ```bash
   uvicorn app.main:app --reload
   ```
   Now head over to `http://localhost:8000`.

---

## 🤝 Join the Forge

We built this for the community. If you found a bug or have an idea for a feature that would make job hunting less of a nightmare, please [open an issue](https://github.com/logeshkannan19/ResumeForge/issues). 

Built with ❤️ for every job seeker out there.
