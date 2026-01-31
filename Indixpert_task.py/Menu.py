listdata=[]
while True:
    print("1. Registration ")
    print("2. Search Student Records ")
    print("3. Exit ")
    choice=int(input("Please Enter Your Choice: "))

    if choice==1:
        student={
                "name":input("Please Enter student's name: "),
                "id":int(input("Please Enter student's id: ")),
                "email":input("Please Enter student's emai: "),
                "address":input("Please Enter student's address: ")
            }
        listdata.append(student)
        print(listdata)
    elif choice==2:
        search_id=int(input("Please Enter Student ID to search for "))
        found_student=False
        for student in listdata:
            if student["id"]==search_id:
                found_student=student
                break
        
        if found_student:
            print(f"\nDetail Found for student ID = {student["id"]}\n-----Searched Student's Details-----\n{found_student}")
        else:
            print("Student's ID not Found!")
    elif choice==3:
        break