from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.doctor import router as doctor_router  
from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()


@router.get("/doctor/{doctor_id}")
def get_doctor(doctor_id: int):

    return {
        "doctor_id": doctor_id,
        "name": "Demo Doctor",
        "specialization": "General Physician"
    }



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