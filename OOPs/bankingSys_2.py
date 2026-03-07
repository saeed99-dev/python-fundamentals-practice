import json
from datetime import datetime


class Banking_system:

    def __init__(self):
        self.balance = 0

    def deposit(self):
        while True:
            try:
                user_input = input("\nPlease enter deposit amount: ")
                credit_amount = int(user_input)

                if credit_amount < 0:
                    print("Error! Amount must be Positive value.")
                else:
                    self.balance += credit_amount
                    print(
                        f"Your account has been credited with Rs :{credit_amount}"
                    )
                    print(f"Your Updated Account Balance is Rs :{self.balance}")
                    break

            except Exception as e:
                print("please Enter the Amoount Carefully.")
                depositlog = {
                    "error": str(e),
                    "time": str(datetime.now()),
                    "operation name": "deposit",
                    "deposit amount": user_input,
                }
                with open("bankcustomlog.txt", "w") as file:
                    json.dump(depositlog, file)

    def withdraw_amount(self):
        while True:
            try:
                user_input = input("\nPlease enter the withdrowal amount: ")
                debit_amount = int(user_input)

                if debit_amount <= self.balance:
                    self.balance -= debit_amount
                    print(f"You have withdrawal amount is Rs: {debit_amount}")
                    print(f"Your Left Account Balance is Rs: {self.balance}")
                    break

                elif debit_amount > self.balance:
                    print("Your Account does not have enough Balance")
                else:
                    print("Error! Amount must be Positive value.")
            except Exception as e:
                print("please Enter the Amoount Carefully.")
                creditlog = {
                    "error": str(e),
                    "time": str(datetime.now()),
                    "operation name": "Withdraw_amount",
                    "deposit amount": user_input,
                }
                with open("bankcustomlog.txt", "w") as file:
                    json.dump(creditlog, file)

    def check_amount(self):
        print(f"\nYour Current A/C Balance is Rs: {self.balance}")


def menu():
    print("\n==== Welcome to Children Bank of India ====\n")
    print("1. Check Balance")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Exit")
    print("="*43)

    return input("Please select your OPtion: ")


def dashboard():

    obj = Banking_system()

    while True:
        try:
            user_input = menu()
            option = int(user_input)

            if option == 1:
                obj.check_amount()
            elif option == 2:
                obj.deposit()
            elif option == 3:
                obj.withdraw_amount()
            elif option == 4:
                print("ThankYou for Visiting! Goodbye! ")
                break
            else:
                print("Please Select Your option carefully!")
        except Exception as e:
            print("please select the option Carefully.")
            user_menu_log = {
                "error": str(e),
                "time": str(datetime.now()),
                "operation name": "Option @ menu",
                "deposit amount": user_input,
            }
            with open("bankcustomlog.txt", "w") as file:
                json.dump(user_menu_log, file)


dashboard()
