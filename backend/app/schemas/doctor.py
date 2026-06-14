
from pydantic import BaseModel, EmailStr, Field


class DoctorBase(BaseModel):

    name: str = Field(
        min_length=3,
        max_length=100,
        description="Doctor full name"
    )

    specialization: str = Field(
        min_length=3,
        max_length=100
    )

    email: EmailStr

    phone: str = Field(
        min_length=10,
        max_length=10,
        description="10 digit phone number"
    )

    experience: int = Field(
        ge=0,
        le=60,
        description="Years of experience"
    )


class DoctorCreate(DoctorBase):

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Dr. John",
                "specialization": "Cardiology",
                "email": "john@gmail.com",
                "phone": "9876543210",
                "experience": 10
            }
        }
    }


class DoctorUpdate(BaseModel):

    name: str | None = None
    specialization: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    experience: int | None = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "experience": 15
            }
        }
    }


class DoctorResponse(DoctorBase):
    id: int

    class Config:
        from_attributes = True