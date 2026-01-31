college_info = ["IIT Delhi", "B.Tech CS", 50000]

name1 = input("Enter Student 1 Name: ")
id1 = (input("Enter Student 1 ID: "))
email1 = input("Enter Student 1 Email: ")
addr1 = input("Enter Student 1 Address: ")

name2 = input("\nEnter Student 2 Name: ")
id2 = (input("Enter Student 2 ID: "))
email2 = input("Enter Student 2 Email: ")
addr2 = input("Enter Student 2 Address: ")

name3 = input("\nEnter Student 3 Name: ")
id3 = (input("Enter Student 3 ID: "))
email3 = input("Enter Student 3 Email: ")
addr3 = input("Enter Student 3 Address: ")

name4 = input("\nEnter Student 4 Name: ")
id4 = (input("Enter Student 4 ID: "))
email4 = input("Enter Student 4 Email: ")
addr4 = input("Enter Student 4 Address: ")

name5 = input("\nEnter Student 5 Name: ")
id5 = (input("Enter Student 5 ID: "))
email5 = input("Enter Student 5 Email: ")
addr5 = input("Enter Student 5 Address: ")

students = [
    {"name": name1, "id": id1, "email": email1, "address": addr1},
    {"name": name2, "id": id2, "email": email2, "address": addr2},
    {"name": name3, "id": id3, "email": email3, "address": addr3},
    {"name": name4, "id": id4, "email": email4, "address": addr4},
    {"name": name5, "id": id5, "email": email5, "address": addr5}
]

print("\n--- Student Records ---")
print(f"College: {college_info[0]}, Course: {college_info[1]}, Fees: ₹{college_info[2]}")
print("\n    Name  -   ID  -    Email    -  Address")
print(f"1. {students[0]["name"]} - ID:{students[0]["id"]} - {students[0]["email"]} - {students[0]["address"]}")
print(f"2. {students[1]["name"]} - ID:{students[1]["id"]} - {students[1]["email"]} - {students[0]["address"]}")
print(f"3. {students[2]["name"]} - ID:{students[2]["id"]} - {students[2]["email"]} - {students[0]["address"]}")
print(f"4. {students[3]["name"]} - ID:{students[3]["id"]} - {students[3]["email"]} - {students[0]["address"]}")
print(f"5. {students[4]["name"]} - ID:{students[4]["id"]} - {students[4]["email"]} - {students[0]["address"]}")
