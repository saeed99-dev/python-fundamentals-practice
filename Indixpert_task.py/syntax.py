# hindi english, math,science, total, percentage, pass>=60% else fail


hindi = int(input("please enter your marks of Hindi: "))
english = int(input("please enter your marks of English: "))
math = int(input("please enter your marks of Math: "))
science = int(input("please enter your marks of Science: "))

# student_marks=[hindi,english,math,science]
# total=sum(student_marks)
total = hindi + english + math + science
percentage = total / 4

if percentage >= 60:
    print("\nResult:Pass!")
else:
    print("\nResult:fail!")



# 
# why are we using dictionary, list, tuple,string,and where we can use it in real life and as well as coding while working for MNCs