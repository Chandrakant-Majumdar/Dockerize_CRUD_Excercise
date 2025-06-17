from fastapi import APIRouter
from app.schemas.student import Student
from app.services import student_service

router = APIRouter()

@router.post("/students/{student_id}")
def create_student(student_id: int, student: Student):
    """
    Create a new student with the given ID and student data.

    Args:
        student_id (int): The unique ID for the student.
        student (Student): The student data to add.

    Returns:
        dict: Success message and the added student data.
    """
    return student_service.create_student(student_id, student)

@router.get("/students/{student_id}")
def read_student(student_id: int):
    """
    Retrieve a student by their ID.

    Args:
        student_id (int): The unique ID for the student.

    Returns:
        Student: The student data if found.
    """
    return student_service.read_student(student_id)

@router.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    """
    Update an existing student's data by their ID.

    Args:
        student_id (int): The unique ID for the student.
        student (Student): The updated student data.

    Returns:
        dict: Success message and the updated student data.
    """
    return student_service.update_student(student_id, student)

@router.delete("/students/{student_id}")
def delete_student(student_id: int):
    """
    Delete a student by their ID.

    Args:
        student_id (int): The unique ID for the student.

    Returns:
        dict: Success message after deletion.
    """
    return student_service.delete_student(student_id)

@router.get("/")
def root():
    """
    Root endpoint providing API information and available endpoints.

    Returns:
        dict: Information about available endpoints and authorship.
    """
    return {
        "endpoints": {
            "Create": "POST /students/{student_id}",
            "Read": "GET /students/{student_id}",
            "Update": "PUT /students/{student_id}",
            "Delete": "DELETE /students/{student_id}"
        },
        "author": "Chandrakant"
    }
