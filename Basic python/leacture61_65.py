# INHERITANCE

# defination :- when one class(child/derivied) derive the properties and method of another class(parent/base).
# parent/base -- this is class that give some code in the annother class
# child/derivied -- this is class that take/inherait all the method and properties

"""
Python Inheritance Syntax
class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class
"""

class person:
    name = "hii yash jain"
    name1 = "anonymous"
    def __hello(self):
        print("hello person")
    def welcome(self):
        self.__hello()
p1 = person()
print(p1.welcome())

class car():
    def __init__ (self , colour, roof , no_door, power):
        self.colour = colour
        self.roof = roof
        self.no_door = no_door
        self.power = power
        # roof ="sdfs"
        print(f"my car colour is {self.colour}")
class Toyatacar(car):         
    colour = "black"
    roof = None
    no_door = 5
    power =  5
    drive = "automatic"
    def col(self):
        print("my car colour is",self.colour)
        # print("my car colour is",colour) raise error
    pass
c = Toyatacar("sdfadfas", None,5,5)
print(c.col())
# class Mother:
#     def __init__(self, mothername):
#         self.mothername =  mothername
 
#     def mother(self):
#         print(self.mothername)
 
 
# class Father:
#     fathername = "asdfsdf"
 
#     def father(self):
#         print(self.fathername)
 
 
# class Son(Mother, Father):
#     def parents(self):
#         print("Father name is :", self.fathername)
#         print("Mother :", self.mothername)
# s1 = Son("hstsrt")
# # s1.fathername = "Mommy"
# # s1.mothername = "Daddy"
# s1.parents()
# s2 = Mother("dfghfh")
# print(s2.mother())

# Access Specifiers/Modifiers

"""
Public Access Specifier in Python
All the variables and methods (member functions) in python are by default public. 
Any instance variable in a class followed by the ‘self’ keyword ie. 
self.var_name are public accessed.
"""
# Example:
class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable
obj = Student(21,"Harry")
print(obj.age)
print(obj.name)

"""
Private Access Modifier
By definition, Private members of a class (variables or methods) are those members which are only accessible inside the class. 
We cannot use private members outside of class.
"""

class Student: 
    def __init__(self, age, name): 
        self.__age = age      # An indication of private variable
        
        def __funName(self):  # An indication of private function
            self.y = 34
            print(self.y)

class Subject(Student):
    pass

obj = Student(21,"Harry")
obj1 = Subject

# calling by object of class Student
# print(obj.__age)          #this is a private so give error
print(obj._Student__age)    #this is a way to use private attriubute
# print(obj.__funName())


class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())

# staticmethod 
# Static methods in Python are methods that belong to a class rather than an instance of the class. 
# They are defined using the @staticmethod decorator and do not have access to the instance of the class (i.e. self). 
# They are called on the class itself, 
# not on an instance of the class. Static methods are often used to create utility functions that don't need access to instance data.

class Math:
  def __init__(self, num):
    self.num = num

  def addtonum(self, n):
    self.num = self.num +n
    
  @staticmethod  # it help to make method without pass self 
  def add(a, b):
      return a + b
a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
 
# way to call static method
print(Math.add(7, 2)) 
print(a.add(7, 2)) 



