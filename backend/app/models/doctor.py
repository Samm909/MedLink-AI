from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.database import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    specialization = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20), unique=True, nullable=False)
    experience = Column(Integer, default=0)
    appointments = relationship(
    "Appointment",
    back_populates="doctor",
    cascade="all, delete"
)