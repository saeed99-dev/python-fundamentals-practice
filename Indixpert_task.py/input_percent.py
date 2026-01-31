Student_name =input("Please Enter Your name: ")


hindi_marks = int(input("\nPlease Enter Your Hindi Marks: "))
eng_marks = int(input("Please Enter Your English Marks: "))
math_marks = int(input("Please Enter Your Math Marks: "))
science_marks = int(input("Please Enter Your Science Marks: "))
computer_marks = int(input("Please Enter Your Computer Marks: "))

total_marks=hindi_marks+eng_marks+math_marks+science_marks+computer_marks

percentage=(total_marks)/5

# print("your percentage is: ",percentage)

print(f"\nDear Mr/Mrs. {Student_name} your total marks is: {total_marks} \nPercentage: {percentage}%")
