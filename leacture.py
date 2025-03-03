class person:
    name = "hii yashjain"
    __name = "anonymous"
    def __hello(self):
        print("hello person")
    def welcome(self):
        self.__hello()
p1 = person()
print(p1.welcome())

#inheritance 
#defination when one class(child/derivied) derive the properties and method of another class(parent/base).
# parent/base -- this is class that give some code in the annother class
class car:                    
    colour = "black"
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stoped")

class Toyatacar(person):         
    def __init__(self,name):
        self.name = name
car1 = Toyatacar("fortuner")
car2 = Toyatacar("prius")
# print(car1.start())
# print(car2.colour)
print(p1.name)



#static method
#this is a decorator
#Method that don't use the self parameter(work at class level)
#like a upper code of a function/method
class cars():
    def __init__(self,number,name):
        self.no= number
        self.na= name
    @staticmethod
    def setting():
        milage= 89 
        print("milage = ",milage)

c1=cars(7,"bmw")
print(c1.no)
print(c1.na)
cars.setting()

# ABSTRACTION , ENCAPSULATION , inheritance, polymosphism
#ABSTRACTION :-
#hiding the implimentation code details of class and only showing the essential features to the user
#just like the engine of the car not show front but we control the engine with the help of parts

#ENCAPSULATION :-
#wrapping data and function into a single unit (object)



# class people():
#     name



#leacture 9 of python 
#del keyword 
# used to delete object properties or object
# del s1.name
# del s1
class student:
    def __init__ (self, semester, year,degree,city):
        self.sem= semester   
        self.yer= year 
        self.cty= city
        self.deg= degree

stu1= student(2,1,"b.tech","vidisha")
# print(stu1.city)    this line give error
# print(student.city) this line give error
print(stu1.cty)
del stu1.cty            #this line delete the item cty from the odject stu1
# print(stu1.cty)         now this line give error

# private(like) attributes and method
# comceptual implementation in python 
# private attributes and method are ment to be used only 
# within the class and are not accessible from outside the class
class account :
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass #(__atribute name) now is private 

        def reset_pass(self):
            print(self.__acc_pass)

acc1=account("1234","abcde")
print(acc1.acc_no)
# print(acc1.__acc_pass)   give error because the '__acc_pass' define as a private
# print(acc1.reset_pass())

