from sqlalchemy.orm import Session

from app.models.appointment import Appointment
from app.models.doctor import Doctor
from app.models.patient import Patient

from app.schemas.appointment import (
    AppointmentCreate,
    AppointmentPatch
)

def create_appointment(
    db: Session,
    appointment: AppointmentCreate
):

    doctor = db.query(Doctor).filter(
        Doctor.id == appointment.doctor_id
    ).first()

    if not doctor:
        return None, "Doctor not found"

    patient = db.query(Patient).filter(
        Patient.id == appointment.patient_id
    ).first()

    if not patient:
        return None, "Patient not found"

    existing = db.query(Appointment).filter(
        Appointment.doctor_id == appointment.doctor_id,
        Appointment.appointment_date == appointment.appointment_date,
        Appointment.appointment_time == appointment.appointment_time
    ).first()

    if existing:
        return None, "Appointment slot already booked"

    new_appointment = Appointment(
        doctor_id=appointment.doctor_id,
        patient_id=appointment.patient_id,
        appointment_date=appointment.appointment_date,
        appointment_time=appointment.appointment_time,
        reason=appointment.reason,
        notes=appointment.notes,
        status="Booked"
    )

    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    return new_appointment, None

def get_all_appointments(db: Session):

    return db.query(
        Appointment
    ).all()

def get_appointment_by_id(
    db: Session,
    appointment_id: int
):

    return db.query(
        Appointment
    ).filter(
        Appointment.id == appointment_id
    ).first()

def delete_appointment(
    db: Session,
    appointment_id: int
):

    appointment = get_appointment_by_id(
        db,
        appointment_id
    )

    if not appointment:
        return False

    db.delete(appointment)
    db.commit()

    return True

def patch_appointment(
    db: Session,
    appointment_id: int,
    appointment_data: AppointmentPatch
):

    appointment = get_appointment_by_id(
        db,
        appointment_id
    )

    if not appointment:
        return None

    update_data = appointment_data.model_dump(
        exclude_unset=True,
        exclude_none=True
    )

    for key, value in update_data.items():
        setattr(
            appointment,
            key,
            value
        )

    db.commit()
    db.refresh(appointment)

    return appointment