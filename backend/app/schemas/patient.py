from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class PatientBase(BaseModel):
    name: str
    age: int
    gender: str
    phone: str
    email: EmailStr
    blood_group: Optional[str] = None
    address: Optional[str] = None


class PatientCreate(PatientBase):
    pass


class PatientUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    blood_group: Optional[str] = None
    address: Optional[str] = None


class PatientResponse(PatientBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True