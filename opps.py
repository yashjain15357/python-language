# class Student:
#     school = "USNHS"  # Class attribute

#     def __init__(self, name, age, marks=None):
#         if marks is None:
#             marks = []  # Initialize with an empty list if no marks are provided
#         self.name1 = name
#         self.age1 = age
#         self.marks1 = marks
#         print(f"This is the information of the student: \n1. Name: {self.name1} \n2. Age: {self.age1}")

    
# # Create instances
# # s1 = Student("raksha", 19, [45, 45, 45])
# # print(Student.school, s1.name, s1.age, s1.marks)

# # s2 = Student("nandni", 45, [85])
# # print(s2.name, s2.age, s2.marks)

# s3 = Student("riya", 19, [99])

# print(s3.name1, s3.age1) 

# class average():
#     def __init__(self,number={[]}):
#         self.number  = number
#         sum =0 
#         for i in number: 
#             sum = sum + i
#         avg= sum/len(number)
#         print(avg)
# a = average([])
class A:
    def method1(self):
        print("A's method")

class B():
    def method2(self):
        print("B's method")

class C():
    def method3(self):
        print("C's method")

class D(B, C,A):
    def method(self):
        print("D's method")

# Create an instance of D and call method
d = D()
d.method()
d.method1()
"""In Object-Oriented Programming (OOP), functions defined within a class are referred to as methods. Methods are crucial components of a class, as they define the behaviors and actions that objects created from the class can perform. There are different types of methods in OOP, each serving a specific purpose:

Types of Methods in Python
Instance Methods
Class Methods
Static Methods
Let's look at each type in detail with examples:

1. Instance Methods
Instance methods are the most common type of methods. They operate on instances of the class and can access and modify the object's attributes. Instance methods are defined with the first parameter as self, which refers to the instance calling the method.

Example:

python
Copy code
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} says Woof!"

    def birthday(self):
        self.age += 1
        return f"Happy Birthday {self.name}! You are now {self.age} years old."

# Create an instance of Dog
my_dog = Dog("Buddy", 3)
print(my_dog.speak())  # Output: Buddy says Woof!
print(my_dog.birthday())  # Output: Happy Birthday Buddy! You are now 4 years old.
In this example, speak and birthday are instance methods. They use the self parameter to access and modify the instance's attributes.

2. Class Methods
Class methods are methods that operate on the class itself rather than on instances of the class. They are defined with the @classmethod decorator and the first parameter is cls, which refers to the class.

Example:

python
Copy code
class Dog:
    species = "Canis lupus familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def species_info(cls):
        return f"All dogs are of the species: {cls.species}"

# Access class method
print(Dog.species_info())  # Output: All dogs are of the species: Canis lupus familiaris
In this example, species_info is a class method. It uses the cls parameter to access the class attribute species.

3. Static Methods
Static methods do not operate on an instance or class directly. They are defined with the @staticmethod decorator and do not take self or cls as the first parameter. Static methods behave like regular functions but belong to the class's namespace.

Example:

python
Copy code
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

# Access static methods
print(MathOperations.add(5, 3))  # Output: 8
print(MathOperations.subtract(10, 4))  # Output: 6
In this example, add and subtract are static methods. They perform operations without needing access to any instance or class-specific data.
d.method2()
d.method3()

# Print the MRO of class D
# print(D.mro())
"""