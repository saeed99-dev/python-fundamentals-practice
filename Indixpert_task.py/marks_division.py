# task: user input student asks 4 subject and find % and give division 60>1st, 45>2nd , 30>3rd, and failed
hindi = int(input("Please Enter Hindi Marks: "))
english = int(input("Please Enter English Marks: "))
math = int(input("Please Enter Math Marks: "))
science = int(input("Please Enter Science Marks: "))

marks = [hindi, english, math, science]
percentage = sum(marks) / len(marks)

if percentage > 60:
    print(f"\nTotal Marks = {sum(marks)}\nPercentage = {percentage}\nDivision = First")
elif percentage > 45:
    print(f"Total Marks = {sum(marks)}\nPercentage = {percentage}\nDivision = Second")
elif percentage > 30:
    print(f"Total Marks = {sum(marks)}\nPercentage = {percentage}\nDivision = Third")
else:
    print(f"Total Marks = {sum(marks)}\nPercentage = {percentage}\nDivision = Failed")
