
class person:
    def __init__(self,name):
        self.name=name
    def emp(self):
        return False
class Employee(person):
    def emp(self):
        return True

class person:
    def __init__(self,name):
        self.__name=name
    def emp(self):
        return False
class Employee(person):
    def __init__(self, name,palace):
        self.__palace=palace
        person.__init__(self,name)
        super().__init__(name)
    def __display(self):
        return f"palace:{self.__palace}\nname:{self.__name}"
    def emp(self):
        return True
class Employee_2(Employee):
    def __init__(self, name, palace,salary):
        super().__init__(name,palace)
        self.__salary=salary
    def _display1(self):
        return self.__salary

    
emp_2=Employee("ali","HR")
emp3=Employee_2("manager","ali",5000)
print(emp_2.__display())
print(emp3.__display1())# not clean code


class A:
    def __init__(self,x):
        self.x=x
    def getx(self):
        return self.x
cond=True
class C(A if cond else object):
    def isA (self):
        return True
ca=(1)
print(ca.isA())


class cssst:
    stream="csc"
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
a=cssst("ali",1)    
print(a.stream)
print(a.name)
cssst.stream="see"
print(a.stream)




class Human:
    def __init__(self,name="no name",age=0,natinalty="no",gender="no"):
        self.name=name
        self.age=age
        self.natinality=natinalty
        self.gender=gender
    def speak(self):
        return f"name:{self.name}\nage:{self.age}\nnatinality:{self.natinality}\ngender:{self.gender}"
class Man(Human):
    def __init__(self, name="no name", age=0, natinalty="no"):
        super().__init__(name, age, natinalty, "male")

bob=Man("ahmed",40,"egpyt")
print(bob.speak())
print("#" * 50)
class Human:
    def __init__(self,name="no name",age=0,natinalty="no",gender="no"):
        self.name=name
        self.age=age
        self.natinality=natinalty
        self.gender=gender
    def speak(self):
        return f"name:{self.name}\nage:{self.age}\nnatinality:{self.natinality}\ngender:{self.gender}"
class Man(Human):
    def __init__(self, name="no name", age=0, natinalty="no"):
        super().__init__(name, age, natinalty, "male")

bob=Man("ahmed",40,"egpyt")
print(bob.speak())
print("#" * 50)




class circle:
    def __init__(self,raduis):
        self.raduis=raduis
    @property
    def area (self):
        return 3.14 * self.raduis**2
    @area.setter
    def area (self,value):
        if value<0:
            raise ValueError("error")
        self.raduis=(value/3.14)**.5
    
        

em1=circle(78.5)
#print(em1.area)
em1.area=-10
print(em1.raduis)




class person:
    word_p="hello"
    def __init__(self,name):
        self.name=name

    def display(self):
        return f"name:{self.name}"
    
e1=person("ahmed")
e2=person("abdo")
print(e1.word_p)
print(e2.word_p)
#######
person.word_p="welcome"
print(e1.word_p)
print(e2.word_p)
######
e1.word_p="test"
print(e1.word_p)
print(e2.word_p)

class person:
    def greet(self):
        print("hello")
class child(person):
    def greet(self):
        print("welcome")

e1=person()
e2=child()
e1.greet()
e2.greet()
############
class person:
    def greet(self):
        print("hello")
class child(person):
    def greet(self):
        return super().greet(),"welcome"
    
e1=person()
e2=child()





def product(a,b):
    p=a*b
    print(p)
def product(a,b,c):
    p=a*b*c
    print(p)

product(5,5)
product(5,6,7)


def sum(datatype,*args):
    if datatype=="int":
        answer=0
        
    if datatype=='str':
        answer=''

    for i in args:
        answer+=i
    print(answer)

sum("int",5,6)
sum("str","hello"," abdo")


from multipledispatch import dispatch
@dispatch(int,int)
def product(a,b):
    result=a*b
    print(result)
@dispatch(int,int,int)
def product(a,b,c):
    result=a*b*c
    print(result)
@dispatch(float,float,float)
def product(a,b,c):
    result=a*b*c
    print(result)


product(9,6)
product(9,6,7)
product(9.7,97.5,78.5)



from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimter(self):
        pass
class rectangle(shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.height * self.width
    def perimter(self):
        return 2*(self.height + self.width)

r=rectangle(5,5)
print(r.area())
print(r.perimter())    