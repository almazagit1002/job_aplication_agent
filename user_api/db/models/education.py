from pydantic import BaseModel
from typing import List, Optional

class Subject(BaseModel):
    subject: str

class EducationEntry(BaseModel):
    start_year: Optional[str]
    end_year: Optional[str]
    degree: str
    institution: Optional[str]
    subjects: List[Subject]
    thesis: Optional[str] = None

class Certification(BaseModel):
    certificate: Optional[str] = None

class CertificationEntry(BaseModel):
    start_year: Optional[str]
    end_year: Optional[str]
    certificates: List[Certification]

