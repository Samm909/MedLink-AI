from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.database.database import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)

    phone = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

    blood_group = Column(String, nullable=True)
    address = Column(String, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )