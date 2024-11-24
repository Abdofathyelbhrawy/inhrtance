class Employee:
    def details (self):
        pass
class manager (Employee):
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary
    def details(self):
        print(f"name:{self.name}\nposition:{self.position}\nsalary:{self.salary}")
class Intern (Employee):
    def __init__(self,name,position,stipend):
        self.name=name
        self.position=position
        self.stipend=stipend
    def details(self):
        print( f"name:{self.name}\nposition:{self.position}\nstipend:{self.stipend}")

Employees=[manager("ahmed","Manager",5000),Intern("ali","intern",1000)]
def display_1(Employees):
    for i in Employees:
        i.details()
display_1(Employees)
    

