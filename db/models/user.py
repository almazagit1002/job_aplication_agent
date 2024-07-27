from pydantic import EmailStr, Field
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime
from enum import Enum

from .base import Timestamp
from .contact_info import ContactInfo
from .education import EducationEntry, CertificationEntry
from .experience import ExperienceEntry
from .skills import SoftSkills, TechSkillsEntry
from .projects import ProjectsEntry


class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"

class User(Timestamp):
    id: UUID = Field(default_factory=uuid4, alias="_id")
    email: EmailStr
    role: Role
    is_active: bool = False
    certifications: List[CertificationEntry]
    contact_info: ContactInfo
    education: List[EducationEntry]
    experience: List[ExperienceEntry]
    projects: List[ProjectsEntry]
    soft_skills: List[SoftSkills]
    technical_skills: List[TechSkillsEntry]
    about_me: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {UUID: str, datetime: lambda v: v.isoformat()}
