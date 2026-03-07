from src.Student.file_mode import load_data,savedata
# from file_mode import load_data,savedata

def Update_records():
    listdata=load_data()
    while True:
        update=input("Do you want to update Student' record? (yes/no): ").lower()
        if update != "yes":
            break
        else:
            search_id=input("Enter Student's ID to update data: ")

            for student in listdata:
                
                if search_id==student["id"]:
                    print("You can Update following Information")
                    print("1. name\n2. Address\n3. Both")
                    option=int(input("Please select Options: "))
                    if  option==1:
                        student["name"]=input("Please Enter New NAme: ")

                    elif option==2:
                        student["address"]=input("Please Enter New Address: ")
                        
                    elif option==3:
                        student["name"]=input("Please Enter New NAme: ")
                        student["address"]=input("Please Enter New Address: ")
                        
                    else:
                        print("PLease Enter valid Optons")
                    
                    savedata(listdata)
                    print(f"Student's data with ID ({search_id}) updated successfully\n")
                    break

                else:
                    print("Invalid Credential!")
            break   
# Update_records()