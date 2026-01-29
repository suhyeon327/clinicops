from pydantic import BaseModel
from datetime import date

class PatientCreate(BaseModel):
    name: str
    birth_date: date