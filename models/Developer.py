from pydantic import BaseModel
from typing import List, Optional
from models.Skill import Skill
from models.Experience import Experience
from models.Language import Language

class Developer(BaseModel):
    _id: str
    name: str
    country: str
    age: int
    skills: List[Skill]
    experience: List[Experience]
    languages: List[Language]
