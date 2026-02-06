import datetime

def menu():
    print("-----Find Reports------")
    print("1. days")
    print("2. Weeks")
    print("3. Months")
    print("4. Years")
    print("5. Exit")

    return 

def get_report():
    while True:
        menu()
        option=int(input("Please Select Your Option: "))
        Today = datetime.date.today()
        x = int(input("Search report number days/weeks/months/years ago(-)/later(+): "))

        if option==1:
            Past_future_date = (datetime.date.today() + datetime.timedelta(days=+(x))).strftime("%d/%m/%Y")
            print(Past_future_date)
        elif option==2:
            Past_future_weeks_date = (datetime.datetime.now() + datetime.timedelta(weeks=+(x))).strftime("%d/%m/%Y")
            print(Past_future_weeks_date)
        elif option==3:
            month_later_ago = (Today.replace(month=Today.month + (x))).strftime("%d/%m/%Y")
            print(month_later_ago)
        elif option==4:
            year_later_ago = (Today.replace(year=Today.year + (x)).strftime("%d/%m/%Y"))
            print(year_later_ago)
        elif option==5:
            print("Exiting Programe....")
            break
        else:
            print("Invalid Option")
            

get_report()

