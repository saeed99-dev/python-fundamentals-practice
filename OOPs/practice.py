# Create a Laptop class with attributes like brand , model , and price .
# 11. Add a discount() method to the Laptop class to reduce the price by a percentage
class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        return f"price \u20b9{self.price},Brand: {self.brand},Model: {self.model}"

    def discount(self, percentage):
        discount_amount = self.price * (percentage / 100)
        self.price -= discount_amount
        return f"Applied {percentage}% discount. New price: \u20b9{self.price:.2f}"


my_laptop = Laptop("Dell", "XPS 26", 75000)
print(my_laptop.display_info())
print(my_laptop.discount(20))


# Create a BankAccount class with deposit and withdraw methods.


class BankAccount:
    def __init__(self):
        self.balance = 1000

    def deposite(self, amount):
        self.balance += amount
        print(
            f"Amound deposited is \u20b9{amount} and the Total Amount is \u20b9{self.balance}"
        )

    def withdrawal(self, amount):
        self.balance -= amount
        print(
            f"Amount withdrawal is \u20b9{amount} and the Total amount is \u20b9{self.balance}"
        )


acc = BankAccount()
acc.deposite(500)
acc.withdrawal(200)


# Create a class StringManipulator with a method to reverse a string.


class StringManipulator:
    def __init__(self, text):
        self.string = text

    def rev_str(self):
        reverse_text = self.string[::-1]
        print(f"The reverse String : {reverse_text}")


rev = StringManipulator("Computer")
rev.rev_str()

# Create a class Clock that stores hours and minutes.


class Clock:
    def __init__(self, hours, minutes):
        self.hours = (hours + (minutes // 60)) % 24
        self.minutes = minutes % 60

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"


my_clock=Clock(14,30)
print(f"the Time is {my_clock}")

# Create a class Temperature that converts Celsius to Fahrenheit.

class Temperature:
    def __init__(self,celcius):
        self.celcius=celcius

    def convert_C_F(self):
        Fahrenheit=(self.celcius*(9/5) + 32)
        print(Fahrenheit)

conv=Temperature(100)
conv.convert_C_F()

