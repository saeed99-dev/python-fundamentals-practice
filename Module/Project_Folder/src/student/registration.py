
listdata=[]
def student_registration():
    student={
        "name": input("Please enter student name: "),
        "id":input("please enter student id "),
        "email":input("please enter student email: "),
        "address":input("please enter student address:")
    }
    listdata.append(student)
    return 

student_registration()