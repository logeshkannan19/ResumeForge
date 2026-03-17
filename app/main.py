from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routes import auth, resumes
from app.utils.database import get_database

# We're keeping things simple with a single FastAPI entry point.
# If this grows, we might want to split these configurations into a separate /app/config.py
app = FastAPI(
    title="ResumeForge AI API",
    description="The engine behind better resumes. Built with a focus on speed and actionable AI feedback."
)

templates = Jinja2Templates(directory="resumeforge/templates")

# standard CORS setup. We're allowing everything for now to make local dev a breeze,
# but we should definitely tighten this up for production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Plugging in our modular routes.
# /auth handles the JWT dance, while /api/resumes does the heavy lifting.
app.include_router(auth.router, tags=["auth"])
app.include_router(resumes.router, prefix="/api", tags=["resumes"])

# Serving static assets like our custom glassmorphism CSS and JS.
app.mount("/static", StaticFiles(directory="resumeforge/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """The landing page. Entry point for the human experience."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("auth.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("auth.html", {"request": request})

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    """The nerve center. Users spend most of their time here."""
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.on_event("startup")
async def startup_db_client():
    # Warming up the MongoDB connection early.
    await get_database()

@app.on_event("shutdown")
async def shutdown_db_client():
    # Cleanup logic goes here if we add persistent connections or background tasks.
    pass
