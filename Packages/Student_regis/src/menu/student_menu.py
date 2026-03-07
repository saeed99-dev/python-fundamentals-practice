from src.student.dashboard import student_registration,remove_student,update_student,display_information

def std_menu():
    print("Welcome to Student Registration Portal")
    print("1. Registration")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Display Information")
    print("5. Exit")

    return int(input("\nPlease Select Option: "))

def student_dashboard():
    while True:
        option=std_menu()
        if option==1:
            student_registration()
        elif option==2:
            remove_student()
        elif option==3:
            update_student()
        elif option==4:
            display_information()
        elif option==5:
            print("Exiting...")
            break
        else:
            print("\nInvalid Credential!")