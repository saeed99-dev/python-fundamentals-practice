import datetime


def get_int_valid(user_input):
    while True:
        value = input(user_input)
        if value.lstrip("-").isdigit() and value != "-":
            return int(value)
        else:
            print("Please Enter Number Only!")


def menu():
    print("\n" + "-" * 5 + "Find Reports" + "-" * 5)
    print("1. days")
    print("2. Weeks")
    print("3. Months")
    print("4. Years")
    print("5. Exit")

    return


def get_report():
    while True:
        menu()
        option = get_int_valid("please Enter Option: ")
        if option == 5:
            print("Exiting Programe....")
            break
        elif option not in [1, 2, 3, 4]:
            print("Invalid Choice")
            continue

        x = get_int_valid("Search report number days/weeks/months/years ago(-)/later(+): ")
        Today = datetime.date.today()

        if option == 1:
            Result = Today + datetime.timedelta(days=x)
        elif option == 2:
            Result = Today + datetime.timedelta(weeks=x)
        elif option == 3:
            total_months = Today.month + x - 1
            new_year = Today.year + (total_months // 12)
            new_month = (total_months % 12) + 1
            Result = Today.replace(year=new_year, month=new_month)
        elif option == 4:
            Result = Today.replace(year=Today.year + (x))

        print(f"Target Date: {Result.strftime('%d/%m/%Y')}")


get_report()
