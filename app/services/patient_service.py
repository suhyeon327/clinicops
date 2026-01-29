from app.repositories.patient_repo import create_patient

def register_patient(db, patient_data):
    # 여기서 비즈니스 로직 추가 가능
    return create_patient(db, patient_data)