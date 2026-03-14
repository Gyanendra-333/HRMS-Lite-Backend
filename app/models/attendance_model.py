from app.database import attendance_collection


def mark_attendance(attendance_data):
    return attendance_collection.insert_one(attendance_data)


def get_attendance_by_employee(employee_id):
    records = []

    for record in attendance_collection.find(
        {"employee_id": employee_id},
        {"_id": 0}
    ):
        records.append(record)

    return records


def delete_employee_attendance(employee_id):
    return attendance_collection.delete_many(
        {"employee_id": employee_id}
    )
