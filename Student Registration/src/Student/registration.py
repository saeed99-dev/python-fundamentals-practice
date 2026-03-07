from time import time
from src.Student.file_mode import create_file,load_data,savedata
from src.Student.validation import valid_email,valid_name

now=str(time())[-5:-1]


def Registation():
    create_file()
    listdata=load_data()
    student = {
            "name": valid_name("Please Enter student's name: "),
            "email": valid_email("Please Enter student's emai: "),
            "address": input("Please Enter student's address: "),
            "id": now
        }
    listdata.append(student)
    savedata(listdata)



    # Registation()