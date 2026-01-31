students_data = []

while True:
    num_input = input("Please Enter the number of students you want to register (1-5): ")

    if num_input.isdigit():
        num = int(num_input)
        if 1 <= num <= 5:
            break
        else:
            print("Out of range! Please enter a number between 1 and 5.")
    else:
        print("Invalid input! Please enter a whole number.")


for i in range(num):
    print(f"\n--- Registering Student {i+1} ---")
    name = input("Please Enter Student Name: ")
    
    while True:
        id_input = input("Please Enter Student ID: ")
        if id_input.isdigit():
            student_id = int(id_input)
            break
        print("Invalid ID! Please use numbers only.")

    email = input("Please Enter Student Email: ")
    address = input("Please Enter Student Address: ")

    student_info = {
        "name": name,
        "id": student_id,
        "email": email,
        "address": address
    }
    
    students_data.append(student_info)

print("\n--- Registered Students ---")
print(students_data)