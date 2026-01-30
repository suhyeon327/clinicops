from fastapi import FastAPI
from app.api.patients import router as patient_router
from app.models.base import Base
from app.database import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(patient_router)