import registration

search_id=int(input("Please enter stdent's ID: "))
for student in registration.listdata:
    if student["id"]==search_id:
        print(f"Detail found for student ID {student["id"]}")
        print(student)
        break
    else:
        print("Student ID not found!")