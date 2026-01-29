from fastapi import APIRouter, Depends
from app.schemas.patient import PatientCreate
from app.services.patient_service import register_patient

router = APIRouter()

@router.post("/patients")
def create_patient_api(patient: PatientCreate):
    # 지금은 DB 연결 생략
    return {
        "message": "환자 생성됨",
        "data": patient
    }