from pydantic import BaseModel
from typing import Optional

class ProjectsEntry(BaseModel):
    start_year: Optional[str]
    end_year: Optional[str]
    project_name: Optional[str]
    project_description: Optional[str] 
    project_link: Optional[str]