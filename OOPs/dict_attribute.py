# Define a class Employee and print its __dict__ attribute.

class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary


emp1 = Employee("Jordan", "Software Engineer", 95000)

print(emp1.__dict__)