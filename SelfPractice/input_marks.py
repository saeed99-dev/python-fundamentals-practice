
marks = int(input("Please Enter Your Marks: "))

if (marks >= 90):
    grade = "A"
elif (marks >= 80 and marks < 90):
    grade = "B"
elif (marks >= 70 & marks < 80):
    grade = "C"
else:
    grade = "D"

print("Grade of the student is ->",grade)


