from sqlalchemy.orm import Session
from app.repositories.patient_repo import create_patient, get_patients

def register_patient(db, patient_data):
    return create_patient(db, patient_data)

def list_patients(db: Session):
    patients = get_patients(db)
    return patients