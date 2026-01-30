from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.patient import PatientCreate
from app.services.patient_service import register_patient
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