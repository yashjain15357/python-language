print("hii yash jain")
# "print" use for print line in a program
print("my name is yash jain","live in sammnapur")

# Escape Sequence Characters
# To insert characters that cannot be directly used in a string, 
# we use an escape sequence character.
# An escape sequence character is a backslash "\" followed by the character you want to insert.
print("this is a line about the new line character \n is a new line character")
print("\ is a new line character")

#print numbers
print("print numbers")
print(123)
print(156)

# More on Print statement
print("hii","hello",5,56 , sep="=") # "sep" is use for seprate the word 
# is like a end =" " is use for the new line character


#print all types of arthematic operators calculation 
print("print all types of arthematic operators calculation ")
print(123+123)
print(123-123)
print(123*123)
print(123/123)

# VARIABLE IN PYTHON
"""
Data types in python 
>> Integer
>> Float
>> String
>> Boolean
>> None
"""
print("STORED VALUE IN VARIABLE")
#stored the values in the variable name
name = "yash jain" #stored string
f= complex(4,9)    # stored complex(a+bi) value
age = 19           # stored integer value
year= 1.23         # stored float  value
old = False        # stored Boolean value
z   = None         # stored None value

""" NOTE the value of the variable stored in the variable name.
 not a variable name is equal to variable value
"""
print("PRINT VALUE IN VARIABLE")
print("my name is ",name)
print("my age is ",age)
print("my year of college is",year)

#print type of variable
print(type(name))
print(type(age))
print(type(year))
print(type(old))
print(type(z))
 #print all types of arthematic operators calculation 
print("Arthematic Operations")
a =15
b = 4
print(a+b)   # Addition
print(a-b)   # Substraction
print(a*b)   # Multiplication
print(a/b)   # Division
print(a%b)   # Remender of a/b
print(a**b)  # a to the power b :-(a^b)
print(a//b)  # a return qusioent

#print all types of Relational operators calculation 
print("Relational Operations")
print(a==b)   # Equal to
print(a!=b)   # Not Equal to
print(a<b)    # Grteaterthan
print(a>b)    # Smallerthan
print(a<=b)   # Grteaterthan Equal to
print(a>=b)   # Smallerthan Equal to

#print all types of Assignment operators calculation 
print("Assignment Operations")
a=b
print("a=b   :",a)   # a=b  now a=4
a+=b
print("a=a+b :",a)   # a=a+b
a-=b
print("a=a-b :",a)   # a=a-b
a*=b
print("a=a*b :",a)   # a=a*b
a/=b
print("a=a/b :",a)   # a=a/b
a%=b
print("a=a%b :",a)   # a=a%b
a**=b
print("a=a**b:",a)  # a=a**b
#Reassign the value of a and b 
a,b=15,4.45 #way of assin the value
 #print all types of Logical operators calculation 
print("Logical Operations")
print(not (a!=b))
print((a>b)and(a!=b))
print((a<b)and(a!=b))
print((a>b)or(a!=b))
print((a<b)or(a==b))


# a =15
# b = 4
# Type conversion
print("Type conversion")
# automatially convert in another data type 
print(a+b) #automatially convert in float data type
print(a/b)

# type casting 
# python support a wide variety of fumcrion sor methods like int()
# float(), str(), ord(), hex(), tuple(), set(), list(), dict(), for the typecasting in python
print("Type casting ")
# with the help of the function convert in another data type
a= float(a)         #manually convert into float data type
print("a=",float(a),type(a))
b=int(b)            #manually convert into int data type
print("b=",int(b),type(b))
c= "465"            # this is a string
print(int(c))       # string convert in the integer

# input by user

name=input("wellcome ")  # input value stored in string data type
age=input ("age :")
year=input("college year :")

print("wellcome",name)
print ("Your age is :",age)
print("Your college year :",year)

print(type(name))
print (type(age))
print(type(year))
# convert input value in string data type to another data type
print("change in another data type")
age = int(age)
year=float(year)

print(type(name))
print (type(age))
print(type(year))

str = "hiiiii"
print(str)
str.replace("h","y")
print(str)

# Take user input in python
# we can take the input by the user by the "input" key word
# "input" function return the user input in the string form
g =input("enter the input ")
print("the type of the 'g' is ",type(g)) # return string type
# for the converting the another data type use typecasting