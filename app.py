# app.py

# from typing import Union
# from pydantic import BaseModel
# from fastapi import FastAPI, HTTPException, Depends
# import sqlite3
# from models.timesheet import Timesheet

from models.timesheet import Timesheet
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlite3 import Connection, connect
from typing import Optional
from models.timesheet import Timesheet

app = FastAPI()

DATABASE_URL = "your_database.db"

# Dependency to get the database connection
def get_db():
    db = connect(DATABASE_URL)
    try:
        yield db
    finally:
        db.close()

# Pydantic model for the request body
class TimesheetCreate(BaseModel):
    employee_id: int
    date_worked: str  # You may want to use date type with validation
    hours_worked: float
    project_code: str
    task_description: str

# Assuming you have Timesheet and Employer classes defined in models
class Timesheet:
    TABLE_NAME = "timesheets"

    def __init__(self, employee_id, date_worked, hours_worked, project_code, task_description):
        self.employee_id = employee_id
        self.date_worked = date_worked
        self.hours_worked = hours_worked
        self.project_code = project_code
        self.task_description = task_description

    def save(self, db: Connection):
        cursor = db.cursor()
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (employee_id, date_worked, hours_worked, project_code, task_description)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (self.employee_id, self.date_worked, self.hours_worked, self.project_code, self.task_description))
        db.commit()
        return cursor.lastrowid

# Endpoint to create a timesheet
@app.post("/timesheets/")
def create_timesheet(timesheet: TimesheetCreate, db: Connection = Depends(get_db)):
    new_timesheet = Timesheet(
        employee_id=timesheet.employee_id,
        date_worked=timesheet.date_worked,
        hours_worked=timesheet.hours_worked,
        project_code=timesheet.project_code,
        task_description=timesheet.task_description
    )
    new_timesheet_id = new_timesheet.save(db)
    return {
        "id": new_timesheet_id,
        "employee_id": new_timesheet.employee_id,
        "date_worked": new_timesheet.date_worked,
        "hours_worked": new_timesheet.hours_worked,
        "project_code": new_timesheet.project_code,
        "task_description": new_timesheet.task_description
    }
app = FastAPI()


# Example endpoint to retrieve timesheets
@app.get("/timesheets/", response_model=list)
def read_timesheets(db: Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM timesheets")
    timesheets = cursor.fetchall()
    return timesheets