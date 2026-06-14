from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.doctor import (
    DoctorCreate,
    DoctorUpdate,
    DoctorResponse,
)
from app.services.doctor_service import (
    create_doctor,
    get_all_doctors,
    get_doctor_by_id,
    update_doctor,
    delete_doctor,
)

router = APIRouter(
    prefix="/doctors",
    tags=["Doctors"],
)


@router.post(
    "/",
    response_model=DoctorResponse,
    summary="Create Doctor",
    description="Create a new doctor record"
)
def add_doctor(
    doctor: DoctorCreate,
    db: Session = Depends(get_db),
):
    return create_doctor(db, doctor)


@router.get(
    "/",
    response_model=list[DoctorResponse],
    summary="Get All Doctors",
    description="Fetch all doctors from database"
)
def read_doctors(
    db: Session = Depends(get_db),
):
    return get_all_doctors(db)


@router.get(
    "/{doctor_id}",
    response_model=DoctorResponse,
    summary="Get Doctor By ID",
    description="Fetch a doctor using the doctor ID"
)
def read_doctor(
    doctor_id: int,
    db: Session = Depends(get_db),
):
    return get_doctor_by_id(db, doctor_id)


@router.put(
    "/{doctor_id}",
    response_model=DoctorResponse,
    summary="Update Doctor",
    description="Update doctor details by ID"
)
def update_doctor_details(
    doctor_id: int,
    doctor: DoctorUpdate,
    db: Session = Depends(get_db),
):
    return update_doctor(
        db=db,
        doctor_id=doctor_id,
        doctor=doctor,
    )


@router.delete(
    "/{doctor_id}",
    response_model=DoctorResponse,
    summary="Delete Doctor",
    description="Delete doctor by ID"
)
def delete_doctor_details(
    doctor_id: int,
    db: Session = Depends(get_db),
):
    return delete_doctor(
        db=db,
        doctor_id=doctor_id,
    )