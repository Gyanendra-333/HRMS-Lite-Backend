from app.database import employee_collection


def create_employee(employee_data):
    return employee_collection.insert_one(employee_data)


def get_employee_by_id(employee_id):
    return employee_collection.find_one({"employee_id": employee_id})


def get_all_employees():
    employees = []
    for emp in employee_collection.find({}, {"_id": 0}):
        employees.append(emp)
    return employees


def delete_employee(employee_id):
    return employee_collection.delete_one({"employee_id": employee_id})