
def registration_menu():
    print("1. Registration ")
    print("2. Search ")
    print("3. Update Student Records ")
    print("4. Delete Student")
    print("5. View Student Records")
    print("6. Exit ")
    
    while True:
        choice = input("Please Select the option: ")

        if choice.isdigit():
            return int(choice)  
        else:
            print("please enter a single digits only!")




