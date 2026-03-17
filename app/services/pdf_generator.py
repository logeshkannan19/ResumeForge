from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
import logging

logger = logging.getLogger(__name__)

class PDFGenerator:
    """Service for generating professional resume PDFs."""

    @staticmethod
    def generate_resume_pdf(data: dict) -> bytes:
        """
        Generate a PDF from resume data.
        
        Args:
            data (dict): Resume content including name, experience, and skills.
            
        Returns:
            bytes: The generated PDF content.
        """
        try:
            buffer = io.BytesIO()
            c = canvas.Canvas(buffer, pagesize=letter)
            width, height = letter
            
            # Header
            c.setFont("Helvetica-Bold", 24)
            c.drawString(50, height - 50, data.get("name", "Name Placeholder"))
            
            c.setFont("Helvetica", 12)
            c.drawString(50, height - 70, f"{data.get('email', '')} | {data.get('phone', '')}")
            
            # Experience Section
            c.setFont("Helvetica-Bold", 16)
            c.drawString(50, height - 110, "EXPERIENCE")
            c.line(50, height - 115, width - 50, height - 115)
            
            y = height - 135
            for exp in data.get("experience", []):
                if y < 100: # Simple page overflow check
                    c.showPage()
                    y = height - 50
                    c.setFont("Helvetica", 10)

                c.setFont("Helvetica-Bold", 12)
                c.drawString(50, y, f"{exp.get('title')} at {exp.get('company')}")
                c.setFont("Helvetica", 10)
                c.drawString(width - 150, y, exp.get("date", ""))
                y -= 15
                c.drawString(60, y, exp.get("description", ""))
                y -= 25
            
            # Skills Section
            y -= 20
            if y < 100:
                c.showPage()
                y = height - 50

            c.setFont("Helvetica-Bold", 16)
            c.drawString(50, y, "SKILLS")
            c.line(50, y - 5, width - 50, y - 5)
            y -= 25
            c.setFont("Helvetica", 12)
            skills_str = ", ".join(data.get("skills", []))
            c.drawString(50, y, skills_str)
            
            c.save()
            buffer.seek(0)
            return buffer.getvalue()
        except Exception as e:
            logger.error(f"Failed to generate PDF: {str(e)}")
            raise RuntimeError("Internal error during PDF generation.")
