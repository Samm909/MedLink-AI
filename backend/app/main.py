from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.doctor import router as doctor_router
from app.api.patient import router as patient_router
from app.api.appointment import router as appointment_router
from app.core.config import settings
from app.database.database import Base, engine
import app.models

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

@app.get("/")
def home():
    return {
        "message": "Welcome to MedLink AI"
    }

app.include_router(health_router)
app.include_router(doctor_router)
app.include_router(patient_router)
app.include_router(appointment_router)