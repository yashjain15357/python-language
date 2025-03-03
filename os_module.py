# if you want to  play the folder so explore the os library.

import os 
#NOTE pass the path of the folder in the os.method_name(path) for the error not generate


# os.mkdir("data")  # make the folder with the help of the "os" library  
'''
for i in range(0 , 100 ):
    os.mkdir(f"data/day{i+1}") # make the 100 folder in the data folder
# rename the folder name
os.rename("data","yash")'''


# see the list of the folder in the folder
# print(os.listdir("yash")) # its print the name in a list form
print("String format :", os.getcwd()) # return the path of the current directiory in string form 
print("\nByte string format :", os.getcwdb()) # return the path of the current directiory in Byte form 

# import os

print("\nCurrent directory :", os.getcwd())

# Changing directory
# os.chdir('c:\Users\YASH JAIN\python language\o_library.py')
# print("Current directory :", os.getcwd())
print("\nThe files in CWD are :",os.listdir(os.getcwd()))   #return all the directory in the last folder of path

print(os.name)
# print(os.path.getsize(os.getcwd()))
# os.link("data")
