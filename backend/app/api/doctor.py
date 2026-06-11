from fastapi import APIRouter

router = APIRouter()


@router.get("/doctor/{doctor_id}")
def get_doctor(doctor_id: int):

    return {
        "doctor_id": doctor_id,
        "name": "Demo Doctor",
        "specialization": "General Physician"
    }

@router.get("/doctors/search")
def search_doctors(
    city: str,
    specialization: str
):
    return {
        "city": city,
        "specialization": specialization,
        "message": "Doctors fetched successfully"
    }