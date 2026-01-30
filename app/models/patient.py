from sqlalchemy import Column, Integer, String, Date
from app.models.base import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birth_date = Column(Date)