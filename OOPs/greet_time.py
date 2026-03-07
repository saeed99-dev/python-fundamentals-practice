from datetime import datetime

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        hour = datetime.now().hour
        
        if hour < 12:
            prefix = "Good morning"
        elif 12 <= hour < 18:
            prefix = "Good afternoon"
        else:
            prefix = "Good evening"
            
        return f"{prefix}, I'm {self.name}."

print(Person("Saeed").greet())