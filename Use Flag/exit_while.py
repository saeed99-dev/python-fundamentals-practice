active=True

while active:
    user_input=input("Please Enter exit to Quit, else continue: ")
    if user_input.lower()=="exit":
        active=False
        print("Goodbye!")
    else:
        print(f"you typed {user_input}")
