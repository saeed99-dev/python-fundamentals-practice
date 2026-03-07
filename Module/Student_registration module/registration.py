import add_student

def student_registration():
    print("\n-----Register 3 Students Data-----")
    for i in range(0,3):
       print(f"\nFill Student{i+1} Data:")
       add_student.add_student_data()


student_registration()