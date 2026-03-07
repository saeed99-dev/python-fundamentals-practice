# validate the following things
#     Name
#     address
#     email


def valid_name(user_nput):
    while True:
        name=input(user_nput)
        if 2>len(name)>50 and name.replace(" ","").isalpha():
            return name
        else:
            ("Invalid Name! Please enter alphabet only")



def valid_digit(user_input):
    while True:
        value = input(user_input)
        if value.isdigit() and value=='5':
            return value
        else:
            print("Please Enter Digits Only and length should be 5 only!")



def valid_email(user_input):
    while True:
        email=input(user_input)
        if email.endswith("@gmail.com"):
            return email
        else:
            print("PLease enter valid email (only gmail is allowed)")

