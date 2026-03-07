from src.Student.file_mode import load_data
from src.Student.validation import valid_digit
# from validation import valid_digit
# from file_mode import load_data


def search_student():
    search_id=valid_digit("Please Enter Student's ID : ")
    listdata=load_data()
    for student in listdata:
        if search_id==student["id"]:
            print(student) 
            return student
        else:
            print("Student ID not Found!")

# search_student()