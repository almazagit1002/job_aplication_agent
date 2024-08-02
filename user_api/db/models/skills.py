from pydantic import BaseModel
from typing import  Optional

class SoftSkills(BaseModel):
    skill: Optional[str]


class TechSkillsEntry(BaseModel):
    tech_skill: Optional[str]
    experinece_time: Optional[int] # 1,2,3,.. (years)
    use_case: Optional[str]