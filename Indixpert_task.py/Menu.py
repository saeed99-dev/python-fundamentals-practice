listdata=[]
while True:
    print("1. Registration ")
    print("2. Search Student Records ")
    print("3. Exit ")
    choice=int(input("Please Enter Your Choice: "))
#    for i in range(1,3):  # check here choice == i and choice itself. why two variable ?
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
        id=int(input("Please Enter Student's ID "))
        #for n in listdata:
            
