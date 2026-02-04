def take_number():
    x = int(input("Please ENter 1st number: "))
    y = int(input("Please ENter 2nd number: "))
    return x, y


def add(x, y):
    print(x + y)


def substract(x, y):
    print(x - y)


def multiply(x, y):
    print(x * y)


def division(x, y):
    if y != 0:
        print(x / y)
    else:
        print("please enter 2nd number !=0")


def menu():
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Division")
    print("5. Exit")

    option = int(input("PLease select any option: "))
    return option


def dashboard():
    while True:
        num = menu()
        if num == 1:
            x, y = take_number()
            add(x, y)

        elif num == 2:
            x, y = take_number()
            substract(x, y)

        elif num == 3:
            x, y = take_number()
            multiply(x, y)

        elif num == 4:
            x, y = take_number()
            division(x, y)
        elif num == 5:
            print("Taking Exit...")
            break
        else:
            print("please enter valide option")


dashboard()
