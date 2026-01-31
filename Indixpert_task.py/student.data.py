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
passing_year_3=int(input("Please Enter 2st student Passing Year: "))

students_data=[
    {id_1:{ "name": name_1, "email": email_1, "degree": degree_1, "year":passing_year_1}},
    {id_2:{"name": name_2, "id": id_2, "email": email_2, "degree": degree_2, "year":passing_year_2}},
    {id_3:{"name": name_3, "id": id_3, "email": email_3, "degree": degree_3, "year":passing_year_3}}
]
input_id=int(input("please Enter Student's ID: "))
print("----------Student's Details---------")
if input_id==id_1:
    print(students_data[0].get(id_1))
elif input_id==id_2:
    print(students_data[1].get(id_2))
elif input_id==id_3:
    print(students_data[2].get(id_3))
else:
    print("Please Enter Valid Student's ID!")


# get sudent data (using get() function) on the basis of ID i.e. just after entering id the student detail should show on the display whose id is entered.