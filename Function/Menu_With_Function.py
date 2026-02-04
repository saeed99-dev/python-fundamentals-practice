import json

listdata = []

def get_int_valid(user_input):
    while True:
        value=input(user_input)
        if value.isdigit():
            return int(value)
        else:
            print("Please Enter Number Only!")

def menu():
    print("1. Registration")
    print("2. View Records")
    print("3. Search Student")
    print("4. Exit")

    return get_int_valid("Please Select Your Option: ")


def student_reg():
    print("------Student's Registration Page------")
    student = {
        "name": input("Please enter student's name: "),
        "id": get_int_valid("Please enter student's ID: "),
        "email": input("Please enter student's Email: "),
        "address": input("Please enter student's Address: "),
        "qualification_name": input("Please enter student's Qualification: "),
        "passing_year": get_int_valid("Please enter Passing Year: "),
    }
    print("Student Registered Successfully!")
    listdata.append(student)


def view_records(listdata):
    print(json.dumps(listdata, indent=4))


def search_student(student):
    search_id = get_int_valid("Please enter student's ID: ")
    for student in listdata:
        if student["id"] == search_id:
            print(f"\nDetail Found for student ID = {student["id"]}")
            print(json.dumps(student, indent=4))
            break
    else:
        print("Student's ID not found!")


def dashboard():
    while True:
        option = menu()
        if option == 1:
            student_reg()
        elif option == 2:
            view_records(listdata)
        elif option == 3:
            search_student(listdata)
        elif option == 4:
            print("Exiting Program....")
            break
        else:
            print("Please Enter Valid Options.")


dashboard()
