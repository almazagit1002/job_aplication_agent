from pydantic import BaseModel
from typing import Optional

class ExperienceEntry(BaseModel):
    start_date: Optional[str]  # Format: YYYY-MM
    end_date: Optional[str] = None  # Format: YYYY-MM
    company: str
    job_type: Optional[str] # Part Time, Internship, Full time
    responsabilities: str