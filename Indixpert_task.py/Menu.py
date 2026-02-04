import json

listdata = []


def get_int_valid(user_input):
    while True:
        value = input(user_input)
        if value.isdigit():
            return int(value)
        else:
            print("Please Enter Number Only!")


while True:
    print("1. Registration ")
    print("2. Search Student Records ")
    print("3. Display Information")
    print("4. Exit ")
    choice = get_int_valid("Please Enter Your Choice: ")

    if 1 <= choice <= 4:
        if choice == 1:
            student = {
                "name": input("Please Enter student's name: "),
                "id": get_int_valid("Please Enter student's id: "),
                "email": input("Please Enter student's emai: "),
                "address": input("Please Enter student's address: "),
                "Qualification": [],
            }
            listdata.append(student)
            while True:
                add_qual = input("Do you want to Add qualification? (yes/no): ").lower()
                if add_qual != "yes":
                    break
                input_qualification = {
                    "Passing_Year": get_int_valid("Please Enter Passing Year: "),
                    "qual_name": input("Please Enter name of Qualification: "),
                }
                student["Qualification"].append(input_qualification)
        elif choice == 2:
            search_id = get_int_valid("Please Enter Student ID to search for ")
            for student in listdata:
                if student["id"] == search_id:
                    print(f"\nDetail Found for student ID = {student["id"]}")
                    print(
                        f"-----Searched Student's Details-----\n{json.dumps(student,indent=4)}"
                    )
                    break
            else:
                print("Student's ID not Found!")
        elif choice == 3:
            print(json.dumps(student, indent=4))
        else:
            print("Exiting Program....")
            break
    else:
        print("Please Enter Whole number between 1-4 only.")
