listdata=[]
def student_registration():
    student = {
                "name": input("Please Enter student's name: "),
                "id": int(input("Please Enter student's id: ")),
                "email": input("Please Enter student's emai: "),
                "address": input("Please Enter student's address: "),
                "qualification":[]
            }
    listdata.append(student)
    print("\nStudent Registered Successfully")

def remove_student():
    remove_id=int(input("Enter Student's ID to delete his/her records: "))
    for student in listdata:
        if student["id"]==remove_id:
            listdata.pop(student["id"])
            listdata.append(student)
    print(f"{student["id"]}\nStudent Removed Successfully")


def update_student():
    while True:
        add_qual=input("Do you want to add qualification (yes/no): ").lower()
        if add_qual!="Yes":
            break
        else:
            input_qual={
                "qual_name":input("Please Enter name of Qualification: "),
                "passing_year":int(input("Please Enter passing year: "))
            }
        listdata["student"]["qualification"].append(input_qual)
        print("\nStudent Updated Successfully")


    


def display_information():
    print("\n----Students Records----")
    print(listdata)

while True:
    option=int(input("Option: "))
    if option==1:
        student_registration()
    elif option==2:
        remove_student()
    elif option==3:
        update_student()
    elif option==4:
        display_information()
    else:
        break
