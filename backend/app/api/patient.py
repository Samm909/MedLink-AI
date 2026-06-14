from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.patient import (
    PatientCreate,
    PatientUpdate,
    PatientResponse,
)
from app.services.patient_service import (
    create_patient,
    get_all_patients,
    get_patient_by_id,
    update_patient,
    delete_patient,
)

router = APIRouter(
    prefix="/patients",
    tags=["Patients"],
)


@router.post(
    "/",
    response_model=PatientResponse,
    summary="Create Patient",
    description="Create a new patient record"
)
def add_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db),
):
    return create_patient(db, patient)


@router.get(
    "/",
    response_model=list[PatientResponse],
    summary="Get All Patients",
    description="Fetch all patients from database"
)
def read_patients(
    db: Session = Depends(get_db),
):
    return get_all_patients(db)


@router.get(
    "/{patient_id}",
    response_model=PatientResponse,
    summary="Get Patient By ID",
    description="Fetch a patient using the patient ID"
)
def read_patient(
    patient_id: int,
    db: Session = Depends(get_db),
):
    return get_patient_by_id(db, patient_id)


@router.put(
    "/{patient_id}",
    response_model=PatientResponse,
    summary="Update Patient",
    description="Update patient details by ID"
)
def update_patient_details(
    patient_id: int,
    patient: PatientUpdate,
    db: Session = Depends(get_db),
):
    return update_patient(
        db=db,
        patient_id=patient_id,
        patient=patient,
    )


@router.delete(
    "/{patient_id}",
    response_model=PatientResponse,
    summary="Delete Patient",
    description="Delete patient by ID"
)
def delete_patient_details(
    patient_id: int,
    db: Session = Depends(get_db),
):
    return delete_patient(
        db=db,
        patient_id=patient_id,
    )