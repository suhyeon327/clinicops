from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.patient import PatientCreate, PatientResponse
from app.services.patient_service import register_patient, list_patients
from app.database import get_db

router = APIRouter()

@router.post("/patients")
def create_patient_api(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):
    created = register_patient(db, patient.dict())
    return {
        "id": created.id,
        "name": created.name
    }

@router.get("/patients", response_model=List[PatientResponse])
def get_patients_api(db: Session = Depends(get_db)):
    return list_patients(db)