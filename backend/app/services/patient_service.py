from sqlalchemy.orm import Session

from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientUpdate
from app.exceptions.custom_exception import (
    PatientNotFoundException,
    PatientEmailAlreadyExistsException,
)


def create_patient(
    db: Session,
    patient: PatientCreate,
):

    existing_patient = (
        db.query(Patient)
        .filter(Patient.email == patient.email)
        .first()
    )

    if existing_patient:
        raise PatientEmailAlreadyExistsException()

    db_patient = Patient(
        name=patient.name,
        age=patient.age,
        gender=patient.gender,
        phone=patient.phone,
        email=patient.email,
        blood_group=patient.blood_group,
        address=patient.address,
    )

    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)

    return db_patient


def update_patient(
    db: Session,
    patient_id: int,
    patient: PatientUpdate,
):

    db_patient = (
        db.query(Patient)
        .filter(Patient.id == patient_id)
        .first()
    )

    if not db_patient:
        raise PatientNotFoundException()

    update_data = patient.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_patient, key, value)

    db.commit()
    db.refresh(db_patient)

    return db_patient


def delete_patient(
    db: Session,
    patient_id: int,
):

    db_patient = (
        db.query(Patient)
        .filter(Patient.id == patient_id)
        .first()
    )

    if not db_patient:
        raise PatientNotFoundException()

    db.delete(db_patient)
    db.commit()

    return db_patient


def get_all_patients(db: Session):

    return db.query(Patient).all()


def get_patient_by_id(
    db: Session,
    patient_id: int,
):

    db_patient = (
        db.query(Patient)
        .filter(Patient.id == patient_id)
        .first()
    )

    if not db_patient:
        raise PatientNotFoundException()

    return db_patient