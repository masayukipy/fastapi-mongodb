from pydantic import BaseModel

class Language(BaseModel):
    name: str
    level: str
