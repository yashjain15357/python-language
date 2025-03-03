# strings
"""in python , anything that you enclose between single or double quotation marks is considered a string
string use indexing or Unicode characters

Note: It does not matter whether you enclose your strings in single or double quotes, 
the output remains the same."""

# Multiline Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#Basic operation of strings
# Concatenation
str1= "Riya"
str2="Goyal"
add_str= (str1+" "+str2)
print(str1+" "+str2) # addition of two string in python
print(add_str) # addition of two string in python

# Length of string
# mean the total number of character in the string including blank space

# str1= "Riya"
# str2="Goyal"
 
print("length of string 1 is :",len(str1))  #(4)
print("length of string 2 is :",len(str2))  #(5)
print("length of added string is :",len(str1+" "+str2))  #(10)
print("length of added string is :",len(add_str))        #(10)

#Concpet of indexing 
name = ("Raksha_Jain") #string
print(name)
print("\ncheck indexing in 'name' string ")
print("first element of string is :",name[0])
print("secound element of string is :",name[1])
print("third element of string is :",name[2])
print("four element of string is :",name[3])
print("five element of string is :",name[4])
print("six element of string is :",name[5])
print("seven element of string is :",name[6])
# print("eighth element of string is :",name[7])
# print("nine element of string is :",name[8])
# print("ten element of string is :",name[9])
# note:- name[4] = b is not allowed b\c string is a inmutable


#Slicing in String
# slicing work with (n-1)
#access a part of string
crush = ("Riya_Goyal")
print("\nPositive Slicing\n")
print(crush)
print(crush[2:6])
print(crush[0:])           #  same as crush[0:len(crush)]
print(crush[:len(crush)])  #  same as crush[0:len(crush)]

print("\nNegative Slicing\n")  # last element is start with a '-1'
print(crush)
print(crush[-6:-2])
print(crush[:-1])           #  same as crush[-len(crush):-1]
print(crush[-len(crush):])  #  same as crush[-len(crush):-1]

print('jump box in string')
print(crush[::-1])
print(crush[-len(crush): :1])




#String functions
string = ("this is a python language by apna college youtube chanel   ") 
print(string.endswith("\nchanel"))       #return Trueif string end with sub string
print(string.endswith("cha"))            #return False if string not end with sub string
print(string.capitalize())               #Make first letter is capital and another letters make small in a string 
print(string.count("a"))                 #return the how many number of time the word/letter repeate
print(string.find("apna"))               #return the first index number of the first occurane  
print(string.replace("python","c"))      #return the new string with changing the word 
print(string.upper())                    #return all the letter of the string in capital letter
print(string.lower())                    #return all the letter of the string in small letter
print(string.strip())                    #remove the leading and traling whitespace
str3 = "Hello !!!"                       #the rstrip() removes any trailing characters
print(str3.rstrip("!"))
print(string.split(" "))                 #returns the separated strings as list items.
str1 = "Welcome to the Console!!!"
print(str1.center(50, "."))








# formate method of string in python 
    # two types for formate string 

# T his is old method 
sentence1 = "hey my name is {} and my crush name is {}"
name = "yash"
crush = "raksha"
print(sentence1.format(name , crush))

# this is a present method 
bestfriend = "riya"
sentence2 = f"hey my name is {name} and my bestfriend name is {bestfriend}"
print(sentence2)
 
price = 69.155646
print(f"the value of product is {price:.3f}") #:.'number'f is used for print up to the decimal value

# docstrings in Python
# Python documentation strings (or docstrings) provide a convenient way of associating documentation with Python modules, functions, classes, and methods. 
# It’s specified in source code that is used, like a comment, to document a specific segment of code.
def my_function():
    '''Demonstrates triple double quotes
    docstrings and does nothing really.'''
  
    return None
 
print("Using __doc__:")
print(my_function.__doc__)
 
print("Using help:")
help(my_function)

# conditional statement 
# if, elif,  else
# SYNTAX OF THE IF ELIF ELSE
"""
if(condition):                                 give tab space in next to condition line
    'code you want in this place'
elif(condition):                               give tab space in next to condition line
    
else:
    code you want in this place'
                                          
note we make the code with only the if statement
but the elif or else not use after the if 
firsst you want use if than capable use elif and if 
"""
# driving vehicle permission
age = int(input("Enter your age :"))
if (age >18):
    print ("You are able to drive the vehicle")
elif(age <18):
    print("You are not able to drive car")
else:
    print ("You are  in a learning mood")   

# Nested if
# if under the if statement is called as nested if

# sort hand if else statement
print("sort hand if else statement")
y= 123
z=123
print("y=",y) if y<z else print("+++++++") if  y>z else print("z=",z)

#                  match case statement
# it just similar to the switch case statement in c or c++ language 
# A match case statement will compare a given variables value to different shapes,
# also referred to as the pattern. in the main idea to keep on comparing the variables 
# with all the preasent patterns until fits into one
#  
#it different with a switch case of c or another language
#it consist a "if " statement in case comparision 

#Example code bar entry
age= int(input("enter your age : "))
match age:
    case 18 :
        print("wellcome sir")
    case _ if age < 18:
        print("soory sir you are not allowed ")
    case _ if age > 18 :
        print("wellcome in bar, sir ")



                    #  this else work for next if statement


# #Grade system in school (Example of Nested if  nn )
# marks= int(input("Enter your percentage :"))

# if(marks>=80 and marks<=100 ):
#     if(marks>=95 and marks<=100):
#         print("your marks is ",marks)
#         print("your grade is A+++")
#     elif(marks>=90 and marks<95):
#         print("your marks is ",marks)
#         print("your grade is A++")
#     elif(marks>=85 and marks<90):
#         print("your marks is ",marks)
#         print("your grade is A+")
#     else:
#          print("your marks is ",marks)
#          print("your grade is A")
# if(marks>=70 and marks<80):
#     if(marks>=75 and marks<80):
#         print("your marks is ",marks)
#         print("your grade is B+")
#     else:
#         print("your marks is ",marks)
#         print("your grade is B")
     
# if(marks>=60 and marks<70):
#     if(marks>=65 and marks<70):
#         print("your marks is ",marks)
#         print("your grade is C+")
#     else:
#         print("your marks is ",marks)
#         print("your grade is C")
# if(marks>=50 and marks<60):
#     if(marks>=55 and marks<60):
#         print("your marks is ",marks)
#         print("your grade is D+")
#     else:
#         print("your marks is ",marks)
#         print("your grade is D")
# if(marks>=40 and marks<50):
#     if(marks>=45 and marks<50):
#         print("your marks is ",marks)
#         print("your grade is E+")
#     else:
#         print("your marks is ",marks)
#         print("your grade is E")
# if(marks>=30 and marks<40):
#     if(marks>=35 and marks<40):
#         print("your marks is ",marks)
#         print("your grade is F+")
#     else:
#         print("your marks is ",marks)
#         print("your grade is F")
# if(marks>=20 and marks<30):
#     if(marks>=25 and marks<30):
#         print("your marks is ",marks)
#         print("your grade is G+")
#     else:
#         print("your marks is ",marks)
#         print("your grade is G")
# if(marks>=10 and marks<20):
#     if(marks>=15 and marks<20):
#         print("your marks is ",marks)
#         print("your grade is H+")
#     else:
#         print("your marks is ",marks)
#         print("your grade is H")
# if(marks>=0 and marks<10):
#     if(marks>=5 and marks<10):
#         print("your marks is ",marks)
#         print("your grade is I+")
#     else:
#         print("your marks is ",marks)
#         print("your grade is I")
# else:
#     print("this is not possible")