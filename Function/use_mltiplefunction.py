def user_input():
    name=input("Please Enter Your name: ")
    id=input("Please Enter Your ID: ")

    return name,id

def user_output(data):
    name,id=data
    print(f"user name={name}\nuser id={id}")

user_output(user_input())


