from fastapi import APIRouter, HTTPException
from app.database import employee_collection, attendance_collection
from app.schemas.employee_schema import Employee

router = APIRouter()

# Add employee


@router.post("/employees", status_code=201)
def add_employee(employee: Employee):

    existing = employee_collection.find_one(
        {"employee_id": employee.employee_id}
    )

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Employee ID already exists"
        )

    employee_collection.insert_one(employee.dict())

    return {
        "message": "Employee created successfully"
    }


# Get all employees
@router.get("/employees")
def get_employees():

    employees = []

    for emp in employee_collection.find({}, {"_id": 0}):
        employees.append(emp)

    return employees


# Delete employee
@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: str):

    employee = employee_collection.find_one(
        {"employee_id": employee_id}
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    employee_collection.delete_one(
        {"employee_id": employee_id}
    )

    attendance_collection.delete_many(
        {"employee_id": employee_id}
    )

    return {
        "message": "Employee deleted successfully"
    }
