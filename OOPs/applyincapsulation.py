class Inventory:
    def __init__(self):
        self.name="Big Bazar"
        self.__onion=20
        self.__patato=15
        
    def view_stocks(self):
        print(f"\nFollowing are the Stocks of {self.name} ")
        print(f"Your Current Stock is in kg: {self.__onion}")
        print(f"Your Current Stock is in kg: {self.__patato}")


    def update_stock(self):
        onion_kg=int(input("Please enter amount of onion you want to add to stock: "))
        self.__onion += onion_kg
        potato_kg=int(input("Please enter amount of potato you want to add to stock: "))
        self.__patato += potato_kg

obj=Inventory()
obj.name="Vishal Megha Mart"
obj.__onion= 35
obj.__patato=45
obj.update_stock()
obj.view_stocks()