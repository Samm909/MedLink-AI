from datetime import date, time
from typing import Optional

from pydantic import BaseModel, ConfigDict


class AppointmentBase(BaseModel):
    doctor_id: int
    patient_id: int

    appointment_date: date
    appointment_time: time

    reason: Optional[str] = None
    notes: Optional[str] = None


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentResponse(AppointmentBase):
    id: int
    status: str

    model_config = ConfigDict(
        from_attributes=True
    )


class AppointmentPatch(BaseModel):
    doctor_id: Optional[int] = None
    patient_id: Optional[int] = None

    appointment_date: Optional[date] = None
    appointment_time: Optional[time] = None

    reason: Optional[str] = None
    notes: Optional[str] = None

    status: Optional[str] = None