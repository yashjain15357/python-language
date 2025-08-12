# if you want to know about the  
"""
The dir() method
dir(): The dir() function returns a list of all the attributes and methods 
(including dunder methods) available for an object. 
It is a useful tool for discovering what you can do with an object. 
Example:
"""

x = [1, 2, 3]
# print for the list 'x'
print(dir(x))   # this print all the method and attribute present in the object 'x'

# The __dict__ attribute
"""__dict__: 
The __dict__ attribute returns a dictionary representation of an object's attributes. 
It is a useful tool for introspection. 
Example:
"""
class Person:
     def __init__(self, name, age):
         self.name = name
         self.age = age

p = Person("John", 30)
# they return the variable name and variable value as a dictionary form
print("\n",p.__dict__,"\n")

# The help() mehthod
"""
help(): 
The help() function is used to get help documentation for an object, 
including a description of its attributes and methods. 
Example:
# """
# print("\n",help(str))
# help("\n",Person)

# super keyword 
# it help to use the parent method in a child method 
# if the method name is same in the parent class or child class
class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    super().__init__( name, id)
    self.lang = lang

rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "2345", "Python")
print(harry.name)
print(harry.id)
print(harry.lang)

class Employee:

  def __init__(self, name):
    self.name = name
# __len__ method
# The len method is used to get the length of an object. 
# This is useful when you want to be able to find the size of a data structure, such as a list or dictionary.
  
  def __len__(self):
    i = 0
    for c in self.name:
      i = i + 1
    return i

# __str__ and __repr__ methods
# The str and repr methods are both used to convert an object to a string representation. 
# The str method is used when you want to print out an object, 
# while the repr method is used when you want to get a string representation of an object that can be used to recreate the object
  
  def __str__(self):
    return f"The name of the employee is {self.name} str"
    
  def __repr__(self):
    return f"Employee('{self.name}')"

# __call__ method
# The call method is used to make an object callable, 
# meaning that you can pass it as a parameter to a function and it will be executed when the function is called. 
# This is an incredibly powerful tool that allows you to create objects that behave like functions.
  def __call__(self):
    print("Hey I am good")

# operator overloading 
class Vector:
  def __init__(self, i, j, k):
    self.i = i
    self.j = j
    self.k = k

  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"
# Inside the __add__ method:
# self is v1 (with i=3, j=5, k=6).
# x is v2 (with i=1, j=2, k=9).
  def __add__(self, x):
    return Vector(self.i + x.i,  self.j+x.j, self.k+x.k) 
v1 = Vector(3, 5, 6)
print(v1)

v2 = Vector(1, 2, 9)
print(v2)

print(v1 + v2)
print(type(v1 + v2))