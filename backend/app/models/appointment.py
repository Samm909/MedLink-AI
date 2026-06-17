from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class Appointment(Base):

    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)

    doctor_id = Column(
        Integer,
        ForeignKey("doctors.id"),
        nullable=False
    )

    patient_id = Column(
        Integer,
        ForeignKey("patients.id"),
        nullable=False
    )

    appointment_date = Column(Date, nullable=False)

    appointment_time = Column(Time, nullable=False)
    reason = Column(String, nullable=True)
    notes = Column(String, nullable=True)



    status = Column(
        String,
        default="Booked"
    )

    doctor = relationship(
        "Doctor",
        back_populates="appointments"
    )

    patient = relationship(
        "Patient",
        back_populates="appointments"
    )