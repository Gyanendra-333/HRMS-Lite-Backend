from pydantic import BaseModel
from datetime import  datetime

class Attendance(BaseModel):
    employee_id: str
    date: datetime
    status: str