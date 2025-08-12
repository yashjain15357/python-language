#Dictionary or set in this file

 # Dictionary in python
"""
Dictionaries are mutable data structures that allow you to store key-value pairs.
Once you have created a dictionary, you can add, remove, or update elements
update elements using the methods dict. update(), dict. pop(), and dict.
 """
print("Dictionary")
info= {
    "name" : "yash",
    "age":20,
    "colleg":"SATI",
    "percentage":78.25
}
print(info)                          #print all the pairs of key:value
print(type(info))                    #print the type of 'info' variable
print(info["name"] )                 #print the value of 'name' key
print(info["percentage"])            #print the value of 'percrntage' key
print(info["age"])                   #print the value of 'age' key
info["age"]=25                       #overwrite / change the value of 'age' key
print(info["age"])                   #print the new value of 'age' key
info["surname"]="jain"               #add new key:value pair 
print(info)                          #print all new-update-old pairs of key:value
info.update()
#Null dictionary
#It is a empty dictionary/ null dictionary
#According to time and uses we add new keys:value

college={}
print(college)
college[1]="name"                    #add '1' as a key and 'name' as a value
print(college)

#Nested dictionary 
print("Nested dictionary")
student_info={
    "name":"yash",
    "class":12,
    "subject":["math","physics","sst","hindi"],
    "marks":{
        "math":96,"physics":69,"sst":99,"hindi":89
    }
}
student_info["marks"]["name"] = 'anj'                  # Adding elements one at a time
print(student_info)
print(len(student_info))                               #Return the total no. of key or lenth of dictionary
print(len(student_info["marks"]))                      #Return the total no. of key or lenth of Nested dictionary["marks"]
print(type(student_info))
print(student_info["marks"]["hindi"])
print(type(student_info["marks"]["hindi"]))

# Different Ways to Create a Python Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)
  
Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)
print(type(Dict))
  
Dict2 = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict2)
print(type(Dict2))

#Dectionary function's in python
"""
student_info={
    "name":"yash",
    "class":12,
    "subject":["math","physics","sst","hindi"],
    "marks":{
        "math":96,"physics":69,"sst":99,"hindi":89
    }
}
"""
print(student_info.keys())           #Print all the keys of the dictionary in a list form not a list data type
print(list(student_info.keys()))     #now the return elements convert in a list form
list1=list(student_info.keys())
print(list1[2])
print(list1[3])
print(type(student_info.keys()))     #print the type of the dictionary function

print("\n")
print(student_info.values())         #Print all the values of the dictionary in a list form not a list data type
list2=list(student_info.values())
print(list2[2])
print(list2[3])
print(type(student_info.values()))

print("\n")
print(student_info.items())         #return all the key:values pairs of the dictionary in a tuple form not a tuple data type
list2=list(student_info.items())
print(list2[2])
print(list2[3])
print(type(student_info.items()))

print("\n")
print(student_info.get("name"))         #return the value of key
print(type(student_info.get("name")))
# Note :- we take access of any key with two type 

print(student_info.get("name")) # if any mistake return None
print(student_info["name"])     # return error if any mistake
# if any mistake the error create so 1 line of code return 'None'
# 2 line of code return 'error'

print("\n")
print("student_info.update({key:value})")
student_info.update({"village":"tendukheda"})       #insert the specified key:value in the dictionary in curly bracket{}
print(student_info.popitem())                       #remove the last key:value in the dictionary 
print(student_info.pop("class"))                    #remove the specified key:value in the dictionary with the help of key

# SET IN PYTHON
"""
A Set in Python programming is an unordered collection data type that is iterable,
mutable and has no duplicate elements.
this print element single time and unorder
This is based on a data structure known as a hash table.
"""
print("\n set in python".upper())
collection={2,4,2,1,"riya","khushi","riya"}                #Collection is a Set
print(collection)                                          # Not print the same value two time
# colleection={}                                          // This is syntax of `Dictionary` not a `Set` 

# Empty Set
collection1 =set()                            # this is a syntax of empty set
print(type(collection1))

# SET FUNCTION IN PYTHON
# collection={2,4,2,1,"riya","khushi","riya"}
print("add method\n",collection1)                   # print all the element of set
collection1.add(3)                   # Add the inmmutable elements in the set not stored a list and set because of the mutablety
collection1.add("raksha")            # Add element in the collection  
collection1.add("riya")              # Add element in the collection  
collection1.add("khushi")            # Add element in the collection  
collection.remove(4)                # Remove element(4) in the collection  

# collection.remove("khushi")       # Remove element("khushi") in the collection  
# print(collection)
print(len(collection))              # print length of Set(collection)/return number of element 

# collection.clear()                # Remove all the element of Set(collection)
print(len(collection))              # print length of Set(collection)/return number of element 

collection.pop()                    # Remove random one element from the Set(collection)
print(collection.pop())             # Print Randomly removed element from the Set(collection)
print(collection)

print(f"union method\n{collection.union(collection1)}")            # **create a union set of two sets(collection and collection1) but not create change in orignal sets

print("insertion method\n",collection.intersection(collection1))   #create a intersection set of two sets(collection and collection1) but not create change in orignal sets

print("symmetric_difference method\n",collection.symmetric_difference(collection1))  #return collection1 element without intersection

print(collection1.issuperset(collection))

print(collection1.issubset(collection))

#remove and discard 
#The main difference between remove and discard is that, 
# if we try to delete an item which is not present in set, then remove() raises an error, 
# whereas discard() does not raise any error.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
cities.discard("Tokyo")
print(cities)

# 'formating' and 'f string' method 
# it is used for the put variable_val between the string 
name = "yash jain"
vil = 'samnapur'
print("this is a old way \nformat-string ".capitalize())
intro = "hii my name is {} and i live in a {} vilage".format(name, vil)
print(intro) # this show the name valur replace by the first bracket and vil replace by the secound
intro = "hii my name is {1} and i live in a {0} vilage".format(name, vil) 
print(intro) # this show the 0 take a name variable and 1 take vil variable


print("this is a updated way \nf-string ".capitalize())
intro = f"hii my name is {name} and i live in a {vil} vilage"
print(intro)

# Docstring in python 
# Python docstrings are the string literals that appear right after the definition of a function, 
# method, class, or module.
#Note :- Doc-string it just define at the starting of the functioin, class etc.

def square(n):
  '''Takes in a number n, returns the square of n'''
  print(n**2)
  # at this place the doc-string is invalid
square(5)
print(square.__doc__)

# PEP 8
#this is a poem 
#import this, type and read this poem