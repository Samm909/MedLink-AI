from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.appointment import (
    AppointmentCreate,
    AppointmentResponse,
    AppointmentPatch,
)

from app.services.appointment_service import (
    create_appointment,
    get_all_appointments,
    get_appointment_by_id,
    patch_appointment,
    delete_appointment,
)

router = APIRouter(
    prefix="/appointments",
    tags=["Appointments"],
)


@router.post(
    "/",
    response_model=AppointmentResponse,
    summary="Create Appointment",
    description="Book a new appointment"
)
def add_appointment(
    appointment: AppointmentCreate,
    db: Session = Depends(get_db),
):
    appointment_obj, error = create_appointment(db, appointment)

    if error:
        raise HTTPException(
            status_code=404,
            detail=error
        )

    return appointment_obj

@router.get(
    "/",
    response_model=list[AppointmentResponse],
    summary="Get All Appointments",
    description="Fetch all appointments"
)
def read_appointments(
    db: Session = Depends(get_db),
):
    return get_all_appointments(db)


@router.get(
    "/{appointment_id}",
    response_model=AppointmentResponse,
    summary="Get Appointment By ID",
    description="Fetch appointment using appointment ID"
)
def read_appointment(
    appointment_id: int,
    db: Session = Depends(get_db),
):
    return get_appointment_by_id(
        db,
        appointment_id,
    )


@router.patch(
    "/{appointment_id}",
    response_model=AppointmentResponse,
    summary="Patch Appointment",
    description="Partially update appointment details"
)
def patch_appointment_details(
    appointment_id: int,
    appointment: AppointmentPatch,
    db: Session = Depends(get_db),
):
    return patch_appointment(
        db=db,
        appointment_id=appointment_id,
        appointment_data=appointment,
    )


@router.delete(
    "/{appointment_id}",
    response_model=AppointmentResponse,
    summary="Delete Appointment",
    description="Delete appointment by ID"
)
def delete_appointment_details(
    appointment_id: int,
    db: Session = Depends(get_db),
):
    return delete_appointment(
        db=db,
        appointment_id=appointment_id,
    )