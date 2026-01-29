from app.models.patient import Patient

def create_patient(db, patient_data):
    patient = Patient(**patient_data)
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient