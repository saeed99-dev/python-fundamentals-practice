class Banking_system:

    def __init__(self):
        self.balance = 0

    def add_amount(self):
        while True:
            user_input = input("Please enter deposit amount: ")
            if user_input.isdigit():
                credit_amount = int(user_input)
                self.balance += credit_amount
                print(f"Your account has been credited with amount :{credit_amount}")
                print(f"Your Updated Account Balance is {self.balance}")
                break
            else:
                print("please Enter Positive Digits Only!")

    def withdrow_amount(self):
        while True:
            user_input = input("Please enter the withdrowal amount: ")

            if user_input.isdigit():
                debit_amount = int(user_input)

                if debit_amount <= self.balance:
                    self.balance -= debit_amount
                    print(f"You have withdrawal amount is :{debit_amount}")
                    print(f"Your Left Account Balance is {self.balance}")
                    break

                elif debit_amount > self.balance:
                    print("Your Account does not have enough Balance")

            else:
                print("please Enter Positive Digits Only!")

    def check_amount(self):
        print(f"Your Current A/C Balance is {self.balance}")


def menu():
    print("1. Check Balance")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Exit")

    user_input = input("Please select your OPtion: ")
    if user_input.isdigit():
        return int(user_input)
    else:
        print("PLease enter digits only!")


def dashboard():

    obj = Banking_system()

    while True:
        option = menu()

        if option == 1:
            obj.check_amount()
        elif option == 2:
            obj.add_amount()
        elif option == 3:
            obj.withdrow_amount()
        elif option == 4:
            print("ThankYou for Visiting! Goodbye! ")
            break
        else:
            print("Please Select Your option carefully!")


dashboard()

# jiska ho gya hai:
#     add exceptional handling
#     and write data and update data
#     log write krwana hai'
#     create a login system if A/C has been created and if not Create a account  FIrst and then move for login
#     for creating account requirement:
#  Name, address, gender, mobile , email, 12digit a/c number
#




