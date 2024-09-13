from fastapi import FastAPI
from typing import Optional
import uvicorn
from pydantic import BaseModel

from sqlalchemy.orm import Session
import models
from database import engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

student = {
    1 : {
        'name':'Deepak',
        'class_yr': 2015
    }
}

class stu_rec(BaseModel):
    name: str
    class_yr: int

# defining the index page of the application
@app.get('/')
def index():
    return "Home Page for creating blogs"



# using path parameters to get the records of a student
@app.get('/records/{student_id}')
def student_records(student_id : int):
    return student[student_id]

# Using query parameters to get the records of the students
@app.get('/student_record')
def query_student_rc(id : int):
    return student[id]

# using post to return the added fields
@app.post('/add_records')
def add_student(name: str, class_yr : int):
    return name,class_yr

# using pydantic base model to add new student records 
@app.post('/py_add_records/{id}')
def add_student(id: int, record: stu_rec):
    if id in student:
        return "id already exists"
    student[id] = record
    return student 
    

# if __name__ == '__main__':
#     uvicorn.run(app,host='127.0.0.1',port = 8000)


