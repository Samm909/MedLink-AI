from fastapi import HTTPException


class DoctorNotFoundException(HTTPException):

    def __init__(self):

        super().__init__(
            status_code=404,
            detail="Doctor not found"
        )

class DoctorEmailAlreadyExistsException(HTTPException):

    def __init__(self):

        super().__init__(
            status_code=409,
            detail="Doctor email already exists"
        )


#------------PATIENT EXCEPTIONS----------------------

class PatientNotFoundException(HTTPException):

    def __init__(self):

        super().__init__(
            status_code=404,
            detail="Patient not found"
        )

class PatientEmailAlreadyExistsException(HTTPException):

    def __init__(self):

        super().__init__(
            status_code=409,
            detail="Patient email already exists"
        )