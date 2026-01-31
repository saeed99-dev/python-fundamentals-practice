name_1=input("Please Enter 1st student name: ")
id_1=int(input("Please Enter 1st student id: "))
email_1=input("Please Enter 1st student emai: ")
degree_1=input("Please Enter 1st student Qualification: ")
passing_year_1=int(input("Please Enter 1st student Passing Year: "))

name_2=input("\nPlease Enter 2nd student name: ")
id_2=int(input("Please Enter 2nd student id: "))
email_2=input("Please Enter 2nd student email: ")
degree_2=input("Please Enter 2nd student Qualification: ")
passing_year_2=int(input("Please Enter 2st student Passing Year: "))

name_3=input("\nPlease Enter 3rd Student name: ")
id_3=int(input("Please Enter 3rd Student id: "))
email_3=input("Please Enter 3rd Student email: ")
degree_3=input("Please Enter 3rd Student degree: ")
passing_year_3=int(input("Please Enter 3rd student Passing Year: "))

students_data=[
    {"name": name_1, "id": id_1, "email": email_1, "degree": degree_1, "year":passing_year_1},
    {"name": name_2, "id": id_2, "email": email_2, "degree": degree_2, "year":passing_year_2},
    {"name": name_3, "id": id_3, "email": email_3, "degree": degree_3, "year":passing_year_3}
]

print("\nFollowing are the Three Given Students Data\n")
print(f"Student-1. [{students_data[0]["name"]} - ID:{students_data[0]["id"]} - {students_data[0]["email"]} - {students_data[0]["degree"]}- {students_data[0]["year"]}]")
print(f"Student-2. [{students_data[1]["name"]} - ID:{students_data[1]["id"]} - {students_data[1]["email"]} - {students_data[1]["degree"]}- {students_data[1]["year"]}]")
print(f"Student-3. [{students_data[2]["name"]} - ID:{students_data[2]["id"]} - {students_data[2]["email"]} - {students_data[2]["degree"]}- {students_data[2]["year"]}]")
