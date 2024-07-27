from pydantic import BaseModel
from typing import Optional


class ContactInfo(BaseModel):
    name: str
    phon_ext: str
    phone: str
    linkedin: Optional[str] = None
    github: Optional[str]  = None
    website: Optional[str]  = None