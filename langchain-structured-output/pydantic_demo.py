from dataclasses import Field
from unittest.loader import defaultTestLoader

from pydantic import BaseModel,EmailStr,Field
from typing import Optional
class Student(BaseModel):
    name:str ='Sujit'
    age:Optional[int]=None
    email:EmailStr
    cgpa:float= Field(gt=0,lt=10,default=5,description='A Rating based on his academic performance')
new_student={"age":32,"email":"abc@gamil.com","cgpa":"9"}

student = Student(**new_student)
print(student.model_dump())
