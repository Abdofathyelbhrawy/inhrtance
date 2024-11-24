class Employee:
    def __init__(self,name1,age1,salary1):
        self.name=name1
        self.age=age1
        self.salary=salary1
    def display (self):
        return f"name:{self.name}\nage:{self.age}\nsalary:{self.salary}"
    def total_1 (self,year1):
        self.year=year1
        total_salar=self.salary + 100*(self.year)
        return f"total_salar: {total_salar}"
em2=Employee("abdo",35,6000)
em1=Employee("ahmed",30,4000)
print(em1.display())
print(em1.total_1(15))
print(em2.display())
print(em2.total_1(20))
print(id(em1))
print(em1)
print(id(em2))
print(em2)
