# OOPS (object oriented programming) IN PYTHON 
# (OOPs) is a programming paradigm that uses objects and classes in programming.
# The main concept of OOPs is 
# to bind the data and the functions that work on that together as a single unit 
# so that no other part of the code can access this data.
"""
OOPs Concepts in Python
Class:-

A class is a blueprint or a template for creating objects, 
providing initial values for state (member variables or attributes), 
and implementations of behavior (member functions or methods). 
The user-defined objects are created using the class keyword.

Objects:-
class is template or blue print, but 
the object is the owner of the class


# four piller of the oops
1 Polymorphism
2 Encapsulation
3 Inheritance
4 Data Abstraction
"""
# Python Class and object 
# class is a blue print of the object

# creating class:
class car():                #creating class 'car'
    colour = "Dark Black"   # Creating attribute 'colour' in the class 'car'
  # colour = "Dark Black"   # Creating attribute also we can say the variables in simple word
    brand = "Lucifer"       # Creating attribute 'brand' in the class 'car'       
print(car.colour)           #print data of the object
print(car.brand)

#Constructors
# A constructor is a special method in a class used to create and initialize an object of a class. 
# There are different types of constructors. 
# Constructor is invoked automatically when an object of a class is created.

# __init__ (): 
# Constructor/ unique function (" called automatically ")
# always return None
# all the class have a function called __init__ () 

#example
class Person:

  def __init__(self, n, o):
    print("Hey I am a person")
    self.name = n
    self.occ = o

  def info(self):
    print(f"{self.name} is a {self.occ}")

# object call the class 
a = Person("Harry", "Developer") # self automatically pass
a.info()

"""
class car():                #creating class 'car'
    def __init__(self):     #this function will execute every time we called  the class
    colour = "Dark Black"   # Creating attribute 'brand' in the class 'car'
    brand = "Lucifer"              
print(car.colour)           #print data of the attribute
print(car.brand)
"""
# with the help of the  __init__() method we can pass the argument and give the new data in the object
# Example with init function
class student():
    school="UNHS" #Class Attributes
    #this is a parameter constructor
    def __init__(self,name,age,marks=[]):
        self.name1= name  #(self.__) if you want to different variable value in every call than use (self.___)
        self.age1 = age   #reference of the object
        self.marks1= marks  #Instance  Attributes or  
        print(f"This is the information of the student 1 name : {self.name1} \n 2 age {self.age1} ")
        #self is the defult parameter

 # Class and Instance Attributes

 # create Method / in built Function
 # Method are  like functions  inside the class
    

    # def method_name(self):
    #     body of code

    def welcome(self):
        print("welcome student ,",self.name1)
    def average(self):
        sum=0
        for a in self.marks1:
            sum = sum+ a
        avg= sum/len(self.marks1)
        print("the average is = ",avg)    

#note : s1, s2 , s3 is a object   
s1=student("raksha",19,[45,45,45])  # this is define the object and also call the class         
print(student.school,s1.name1,s1.age1,s1.marks1)
s1.welcome()                          #calling the method using dot operator
s2=student("nandni",45,[85])
print(s2.name1,s2.age1,s2.marks1)
s3=student("riya",19,99)
print(s3.name1,s3.age1,s3.marks1)
s2.average()
s1.average()

# Decorators in Python
#  it allows programmers to modify the behaviour of a function or class. 
#  wrap another function in order to extend the behaviour of the wrapped function, 
#  without permanently modifying it

# getters and setters in python
 
# Getters
# Getters in Python are methods that are used to access the values of an object's properties. 
# They are used to return the value of a specific property, and are typically defined using the @property decorator. 
# Here is an example of a simple class with a getter method:

class MyClass:
    def __init__(self, value):
        self._value = value
    @property
    def value(self):
        return self._value
# In this example, the MyClass class has a single property, _value, which is initialized in the init method. 
# The value method is defined as a getter using the @property decorator, and is used to return the value of the _value property.

# To use the getter, we can create an instance of the MyClass class, and then access the value property as if it were an attribute:

# >>> obj = MyClass(10)
# >>> obj.value
# 10
# Setters
# It is important to note that the getters do not take any parameters and we cannot set the value through getter method.
# For that we need setter method which can be added by decorating method with @property_name.setter

# Here is an example of a class with both getter and setter:

class MyClass:
    def __init__(self, value):
        self._value = value
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, new_value):
        self._value = new_value
# We can use setter method like this:

# >>> obj = MyClass(10)
# >>> obj.value = 20
# >>> obj.value
# 20
# In conclusion, getters are a convenient way to access the values of an object's properties, 
# while keeping the internal representation of the property hidden. 
# This can be useful for encapsulation and data validation.



