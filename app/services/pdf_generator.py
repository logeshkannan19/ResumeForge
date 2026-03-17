from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

class PDFGenerator:
    @staticmethod
    def generate_resume_pdf(data: dict) -> bytes:
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter
        
        # Header
        c.setFont("Helvetica-Bold", 24)
        c.drawString(50, height - 50, data.get("name", "Name Placeholder"))
        
        c.setFont("Helvetica", 12)
        c.drawString(50, height - 70, f"{data.get('email', '')} | {data.get('phone', '')}")
        
        # Experience
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, height - 110, "EXPERIENCE")
        c.line(50, height - 115, width - 50, height - 115)
        
        y = height - 135
        for exp in data.get("experience", []):
            c.setFont("Helvetica-Bold", 12)
            c.drawString(50, y, f"{exp.get('title')} at {exp.get('company')}")
            c.setFont("Helvetica", 10)
            c.drawString(width - 150, y, exp.get("date", ""))
            y -= 15
            c.drawString(60, y, exp.get("description", ""))
            y -= 25
        
        # Skills
        y -= 20
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, y, "SKILLS")
        c.line(50, y - 5, width - 50, y - 5)
        y -= 25
        c.setFont("Helvetica", 12)
        c.drawString(50, y, ", ".join(data.get("skills", [])))
        
        c.save()
        buffer.seek(0)
        return buffer.getvalue()
