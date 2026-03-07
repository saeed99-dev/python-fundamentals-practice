try:
    age=int(input("Please enter your age: "))
except Exception as e:
    print("that's not a number.")
    print(e)
