from fastapi import APIRouter, HTTPException
from app.database import attendance_collection, employee_collection
from app.schemas.attendance_schema import Attendance

router = APIRouter()

VALID_STATUS = ["Present", "Absent", "Leave"]


# Mark attendance
@router.post("/attendance", status_code=201)
def mark_attendance(attendance: Attendance):

    employee = employee_collection.find_one(
        {"employee_id": attendance.employee_id}
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee does not exist"
        )

    if attendance.status not in VALID_STATUS:
        raise HTTPException(
            status_code=400,
            detail="Invalid attendance status"
        )

    attendance_collection.insert_one(attendance.dict())

    return {
        "message": "Attendance recorded successfully"
    }


# Get attendance for employee
@router.get("/attendance/{employee_id}")
def get_attendance(employee_id: str):

    employee = employee_collection.find_one(
        {"employee_id": employee_id}
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    records = []

    for record in attendance_collection.find(
        {"employee_id": employee_id},
        {"_id": 0}
    ):
        records.append(record)

    return records
