from sqlalchemy.orm import Session
from app.models.patient import Patient

def create_patient(db: Session, patient_data: dict):
    patient = Patient(**patient_data)
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

def get_patients(db: Session):
    return db.query(Patient).all()