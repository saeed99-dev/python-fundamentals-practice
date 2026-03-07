listadata=[]

def add_student_data():
    student = {
        "name": input("\nPlease Enter student's Name: "),
        "id": input("Please Enter student's ID: "),
        "email": input("Please Enter student's Email: "),
        "address": input("Please Enter student's Address: "),
    }
    listadata.append(student)
    print("Student Record Saved")
    return student
