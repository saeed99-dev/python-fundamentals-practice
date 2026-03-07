#Instantiate three different objects of a Car class.
class Car:
    def __init__(self,brand,model,year,color):
        self.brand=brand
        self.model=model
        self.year=year
        self.color=color
        

    def display_info(self):
        return f"{self.year} {self.brand} {self.model} {self.color}"
    

car_1=Car("Tata","harrier",2021,"Black")
car_2=Car("mahindra","Scorpio",2020,"While")
car_3=Car("Landrover","Defennder",2010,"White")

print(car_1.display_info())
print(car_2.display_info())
print(car_3.display_info())