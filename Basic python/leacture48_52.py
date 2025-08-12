# local and global variables
'''A local variable is a variable that is defined within a function and is only accessible within that function. 
It is created when the function is called and is destroyed when the function returns.

On the other hand, a global variable is a variable that is defined outside of a function and is accessible from within any function in your code.'''

x = 10 # global variable
def my_function():
  y = 5 # local variable
  print(y)
my_function()
print(x)
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function

# The global keyword
x = 10 # global variable

def my_function():
  global x
  x = 5 # this will change the value of the global variable x
  y = 5 # local variable

my_function()
print(x) # prints 5
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function
# file input output
#  file I/O in python
# python can be used to perform operation on a file.(read and write)
# in this chapter we read 
# how can we read the file 
# how can we open the file
# how can we close the file
# how can we delete the file
# 
# Text file : data stored in the character form 
#           : example .txt , .docx ,.log etc.
# Binary file : data stored in another form but not in a character form 
#              example .mp4 , .mov, .png, .jpeg etc . 
# 
# Note: in the ram all the file stored in the 0,1 form  

'''
There are various modes in which we can open files.

read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.

write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

create (x): This mode creates a file and gives an error if the file already exists.

text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).

binary (b): used to handle binary files (images, pdfs, etc).
'''
#READ TO THE FILE
print("\n\nfile handling in python \n\n".capitalize())
# read mode is a default mode
f=open("love_life.txt","r")
a= f.read()
print("\n",a)
print("\n",type(a))
f.close()

f=open("love_life.txt","r").read()
print("\n",f)
print("\n",type(f))
open("love_life.txt","r").close()

f=open("love_life.txt","r")  
b= f.read(5)   # read only 5 character from the string 
print(b)       # print 5 character from the file
b= f.readline()# read the single line by line 
print(b)       # print the data of the file and also print the blank line
               # because the '\n' work after the line
f.close()
# WRITE TO A FILE

# write mode 
f = open("love_life.txt","w") # The write mode delete all the data from the file 
f.write("abc")                # this line write the data in the file 
f.close()
# Append mode
#  this mode add the line or character in the file without deleting the data in the exiesting file
f= open("love_life.txt","a")  # open the file in the append mode
f.write("\ni love you")       # add the line or character in the file at the of the file
f.close()
# r+:  To read and write data into the file. The previous data in the file will be overridden.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It won’t override existing data.
f= open("love_life.txt","r+")  #open in read  and write mode (r+)
f.write("HIII\n this is the love life of my crush")        # over write the line in this mode
f.close()


#  (WITH) SYNTAX
# with open("demo.txt","mood of open") asv(name of variable):
        # data = f.read
        # print(data)
with open("macro.txt","r")as d:  # == f=open("love_life.txt","r")
    print(d.read())
# no need to close the file in with statement

# Deleting a File
# using the os module
# Module (like a code library) is a file written by another programmer that generally has

# import os
# os.remove("love_life.txt")

# Create a new file “practice.txt” using python. Add the following data in it:
with open("pratice.txt","w")as a :
    b=a.write("Hi everyone \nwe are learning file I/O\nusing java\ni love programing in java\n")
    print(b)
a.close

# use some method for read or write the file 

with open("pratice.txt",'r') as a:
    a.seek(5)       # skip the the 5 byte because of the see(5)
    print(a.read(9))#print the next 9 bytes
    print(a.tell()) # print how much bytes we move in file
    a.close
with open("love_life.txt",'w') as a:
    a.write("0123456789ot filled gjgjjhjhgjh")
    a.truncate(10) # this method do fix the size of the file
                   # and remove all the data if it is over the size
with open("love_life.txt",'r') as a:
     print(a.read())
     a.close

with open ('macro.txt','a')as b: 
    print(b.write("hiiiiiiiiiiiiiiiiiiiiiiiiiiii"))
    b.close

f = open('c.txt', 'r')
i = 0
while True:
  i = i + 1
  line = f.readline() # read the full line of the file 
  if not line:        #after the last line break the loop 
    break             # read the blank line if the come 
  m1 = int(line.split(",")[0])
  m2 = int(line.split(",")[1])
  m3 = int(line.split(",")[2])
  print(f"Marks of student {i} in Maths is: {m1*2}")
  print(f"Marks of student {i} in English is: {m2*2}")
  print(f"Marks of student {i} in SST is: {m3*2}")

  print(line)

f = open('myfile2.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)        
f.close()