# 1. check positive or negative of a number

number = int(input("Please enter any number: "))
if number > 0:
    print(f"{number} is a +ve number.")
else:
    print(f"{number} is a -ve number.")

# 2.  print the larger number among the given two number
a = int(input("Please enter any number A: "))
b = int(input("Please enter any number B: "))

if a > b:
    print(f"{a} is greater")
else:
    print(f"{b} is greater")

# 3. check vote eligibility, min age=18
age = int(input("Please enter your age: "))
if age > 18:
    print("eligible for vote!")
else:
    print("Not eligible for vote!")

# 4. check a year is leap year or not.
year = int(input("Please enter year: "))
if year % 4 == 0:
    print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year!")

# 5. grade recieved

marks = int(input("Please enter marks: "))
if marks >= 60:
    print("Pass")
else:
    print("Fail")

# 6.  password match
saved_password = "Saeed123"
user_input = "Saeed123"
if user_input == saved_password:
    print("Access Granted")
else:
    print("Access Denied")

# 7. stock alert

eggs = int(input("please check egg availability: "))
if eggs < 5:
    print("Time to go grocery shopping!")
else:
    print("Enough Reserve available!")


# 9. Free Shipping above Rs 100
cart_total = float(input("please check cart value: "))
if cart_total > 100.00:
    print("You qualify for free shipping!")
else:
    print("You are not qualify for free shipping!")

# 10. Traffic Light Red, Green, Yellow
light = "Red"
if light == "Green":
    print("Go")
elif light == "Yellow":
    print("Slow Down")
elif light == "Red":
    print("Stop")


# 11. 24 hours Time division
hour = int(input("plese enter time: "))
if 5 <= hour <= 11:
    print("Good Morning")
elif 12 <= hour <= 17:
    print("Good Afternoon")
elif 18 <= hour <= 22:
    print("Good Evening")
else:
    print("Good Night")
