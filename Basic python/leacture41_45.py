# short hand if else 
#this is short form
# result = value_if_true if condition else value_if_false

# this is a long form of code
''' if condition:
        result = value_if_true
    else:
        result = value_if_false'''

a = 330
b = 330
#this is short form
print("A") if a > b else print("=") if a == b else print("B")
# this is a long form of code
if a> b :
    print("A")
elif a== b :
    print ("=")
else :
    print ("B")

#this is short hand if else 

#Enumarate function
'''The enumerate function is a built-in function in Python 
that allows you to loop over a sequence (such as a list, tuple, or string) 
and get the index and value of each element in the sequence at the same time. 
Here's a basic example of how it works:

'''
print("Enumarate function")
marks = [12, 56, 32, 98, 12,  45, 1, 4]

# index = 0
# for mark in marks:
#   print(mark)
#   if(index == 3):
#     print("Harry, awesome!")
#   index +=1

for index, mark in enumerate(marks, start=1):
  print(mark)
  if(index == 3):
    print("Harry, awesome!")

# virtual enviroment in python
#Create Virtual Environment in Python
#pip install virtualenv
#virtualenv (directory name)
# virtualenv -p /usr/bin/python3 myenv
# Activate the Virtual Environment:
# myenv\Scripts\activate
# Deactivate the Virtual Environment:
# deactivate

# How importing in python works
# way 1st to import 
import math                  # it import all the method of library
result = math.sqrt(9)
print(result)  # Output: 3.0

# way 2st to import with the "from" keyword 
from math import sqrt       # import specific functions or variables from a module using the 'from' keyword
result = sqrt(9)
print(result)  # Output: 3.0

from math import sqrt, pi
result = sqrt(9)
print(result)  # Output: 3.0
print(f"{pi}")  # Output: 3.141592653589793

# way 3rd to import with nickname with the help of "as" keyword 
import math as m
result = m.sqrt(9)
print(result)  # Output: 3.0
print(m.pi)  # Output: 3.141592653589793

# # if__name__=="__main__"

import leacture20_21    # this line run all the method or code inside the file
# for stop the auto run of file we use 'if__name__=="__main__" '
# in the "average" method we not use'if__name__=="__main__"' so the method run without call 
# always check the all unknow method
a=leacture20_21.fac(5)
print(a)
b=leacture20_21.sum()
print(b)