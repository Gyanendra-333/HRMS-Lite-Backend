from pymongo import MongoClient

MONGO_URL = "mongodb+srv://pgyanendra333_db_user:65eerxipc1qZ9QKQ@cluster0.jrt3gqz.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URL)

db = client["hrms_db"]

employee_collection = db["employees"]
attendance_collection = db["attendance"]


