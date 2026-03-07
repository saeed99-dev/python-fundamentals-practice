from calc_logic import add,substract,multiply,divide

def menu():
    print("1. Add")
    print("2. Substract")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    return int(input("Please Select option: "))

def dashboard():
    while True:
        option=menu()

        if 1<option>5:
            print("Invalid Option!")
            continue
        elif option==5:
            print("Exiting...")
            break
        num1=int(input("Please Enter 1st Number: "))
        num2=int(input("Please Enter 2nd Number: "))
        if option==1:
            add(num1,num2)
        elif option==2:
            substract(num1,num2)
        elif option==3:
            multiply(num1,num2)
        elif option==4:
            divide(num1,num2)


dashboard()
