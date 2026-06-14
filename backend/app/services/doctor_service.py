from sqlalchemy.orm import Session

from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate, DoctorUpdate
from app.exceptions.custom_exception import (
    DoctorNotFoundException,
    DoctorEmailAlreadyExistsException,
)


def create_doctor(db: Session, doctor: DoctorCreate):
    existing_doctor = (
    db.query(Doctor)
    .filter(Doctor.email == doctor.email)
    .first()
)

    if existing_doctor:
        raise DoctorEmailAlreadyExistsException()

    db_doctor = Doctor(
        name=doctor.name,
        specialization=doctor.specialization,
        email=doctor.email,
        phone=doctor.phone,
        experience=doctor.experience,
    )

    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)

    return db_doctor


def update_doctor(
    db: Session,
    doctor_id: int,
    doctor: DoctorUpdate,
):

    db_doctor = (
        db.query(Doctor)
        .filter(Doctor.id == doctor_id)
        .first()
    )

    if not db_doctor:
        raise DoctorNotFoundException()

    update_data = doctor.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_doctor, key, value)

    db.commit()
    db.refresh(db_doctor)

    return db_doctor


def delete_doctor(
    db: Session,
    doctor_id: int,
):

    db_doctor = (
        db.query(Doctor)
        .filter(Doctor.id == doctor_id)
        .first()
    )

    if not db_doctor:
        raise DoctorNotFoundException()

    db.delete(db_doctor)
    db.commit()

    return db_doctor


def get_all_doctors(db: Session):

    return db.query(Doctor).all()


def get_doctor_by_id(
    db: Session,
    doctor_id: int,
):

    db_doctor = (
        db.query(Doctor)
        .filter(Doctor.id == doctor_id)
        .first()
    )

    if not db_doctor:
        raise DoctorNotFoundException()

    return db_doctor