import pdfplumber
import docx
from typing import str
import io

class FileParser:
    @staticmethod
    def parse_pdf(file_content: bytes) -> str:
        text = ""
        with pdfplumber.open(io.BytesIO(file_content)) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text

    @staticmethod
    def parse_docx(file_content: bytes) -> str:
        doc = docx.Document(io.BytesIO(file_content))
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text

    @classmethod
    def parse_file(cls, file_content: bytes, filename: str) -> str:
        if filename.endswith(".pdf"):
            return cls.parse_pdf(file_content)
        elif filename.endswith(".docx"):
            return cls.parse_docx(file_content)
        else:
            raise ValueError("Unsupported file format")
