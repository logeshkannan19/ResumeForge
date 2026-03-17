import pdfplumber
import docx
import io
import logging

logger = logging.getLogger(__name__)

class FileParser:
    """Service for parsing text from various file formats (PDF, DOCX)."""

    @staticmethod
    def parse_pdf(file_content: bytes) -> str:
        """
        Extract text from a PDF file.
        
        Args:
            file_content (bytes): The binary content of the PDF file.
            
        Returns:
            str: The extracted text.
        """
        text = ""
        try:
            with pdfplumber.open(io.BytesIO(file_content)) as pdf:
                for page in pdf.pages:
                    text += (page.extract_text() or "") + "\n"
        except Exception as e:
            logger.error(f"Failed to parse PDF: {str(e)}")
            raise ValueError("Could not parse PDF content.")
        return text

    @staticmethod
    def parse_docx(file_content: bytes) -> str:
        """
        Extract text from a DOCX file.
        
        Args:
            file_content (bytes): The binary content of the DOCX file.
            
        Returns:
            str: The extracted text.
        """
        try:
            doc = docx.Document(io.BytesIO(file_content))
            text = ""
            for para in doc.paragraphs:
                text += para.text + "\n"
        except Exception as e:
            logger.error(f"Failed to parse DOCX: {str(e)}")
            raise ValueError("Could not parse DOCX content.")
        return text

    @classmethod
    def parse_file(cls, file_content: bytes, filename: str) -> str:
        """
        Parse a file based on its extension.
        
        Args:
            file_content (bytes): Binary file content.
            filename (str): Original filename to determine type.
            
        Returns:
            str: Extracted text.
        """
        if filename.lower().endswith(".pdf"):
            return cls.parse_pdf(file_content)
        elif filename.lower().endswith(".docx"):
            return cls.parse_docx(file_content)
        else:
            raise ValueError("Unsupported file format. Please upload PDF or DOCX.")
