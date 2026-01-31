
# user input student id, name, address and verify them with isalpha, 
# studentid must be =18digits---use zfill
title=print("Please Enter The Following Details\n")
name1 = input("Enter Student 1 Name: ")
id1 = (input("Enter Student 1 ID: "))
address1 = input("Enter Student 1 Address: ")

name2 = input("\nEnter Student 2 Name: ")
id2 = (input("Enter Student 2 ID: "))

address2 = input("Enter Student 2 Address: ")

student=[
    {"name":name1.isalpha(), "id":id1.zfill(18), "address":address1.isalnum()},
    {"name":name2.isalpha(), "id":id2.zfill(18), "address":address2.isalnum()}
]

print(f"\n1. {student[0]["name"]}, {student[0]["id"]}, {student[0]["address"]}")
print(f"2. {student[1]["name"]}, {student[1]["id"]}, {student[1]["address"]}")

