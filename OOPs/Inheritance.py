# class Human:
#     def __init__(self,num_heart):
#         self.num_eye=2
#         self.num_nose=1
#         self.num_heart=num_heart

#     def eat(self):
#         print("I can eat")

#     def work(self):
#         print("I can work")


# class Male(Human):
#     def __init__(self,name,heart):
#         super().__init__(heart)
#         self.name=name

#     def flirt(self):
#         print("I can flirt")

#     def work(self):
#         super().work() # it will print super class work as well
#         print("I can code")

#     def display(self):
#         print(f"Hi, i am {self.name} and i have {self.num_heart} heart")


# male_1=Male("Aakash",1)
# male_1.flirt()
# male_1.work()
# print(male_1.num_eye)
# print(male_1.num_nose)
# male_1.display()




# class Human:
#     def eat(self):
#         print("Can eat")
    
#     def work(self):
#         print("Can Work")
    
#     def speak(self):
#         print("Can Speak")

# class Shivam(Human):
#     def qualification(self):
#         print("he has completed B.Tch")

#     def locality(self):
#         print("he is from Bihar")

# class Asif(Shivam):
#     def profession(self):
#         print("he is an Engineer")


# obj=Asif()
# obj.eat()
# obj.speak()
# obj.qualification()
# obj.locality()
# obj.profession()




class Book:
    def material(self):
        print("Generally, it is made up of wood")

    def availability(self):
        print("Available @ Library or @ Book shop")

class Social_Science(Book):
    def content(self):
        print("it studies of people in society")

class History(Social_Science):
    def content(self):
        print("it studies the past Events")

ob=History()
ob.material()
ob.availability()
ob.content()
