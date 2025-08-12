#list and  tuples 

#topic :- List in Python
"""
Indexing is same a string indexing 
reassin the value in the list with the help of the of the indexing number (called as mutationn)
but not allowed in a string  
it can able to stored element of different data type
Mutating methods are ones that change the object after the method has been used
"""
information=['Raksha',19,'indore','2nd year']  
print (information)
# take access of element by indexing
print(information[0])
print(information[2])
print(information[1])

# change information of list's element by indexing
information[0] ="Riya"          #change Raksha to Riya
information[1] =18              #change 19 to 18
information[2] ='tendukheda'    #change indore to tendukheda
information[3] ='4th semester'  #change '2nd year' to '4th semester'
# this thing not allowed in a string(Python language)
print(information) # all new values print at that time

#Slicing in List
# same to same as a string slicing
#acces a part of List
print(information)
print("Positive Slicing")
print(information)
print(information[2:6])
print(information[0:])           #  same as information[0:len(information)]
print(information[:len(information)])  #  same as information[0:len(information)]

print("Negative Slicing")
print(information)
print(information[-6:-2])
print(information[:-1])           #  same as information[-len(information):-1]
print(information[-len(information):])  #  same as information[-len(information):-1]

#List Functions in python 
number =[9,5,8,6,4,7,1,2,3]
character =['f','a','e','b','d','c']
print(number)
# list function is only able to change in list 
# it is not able to directly print like "print(number.append(10))"
# >>> "print(number.append(10))" it's a None data type
# >>> first apply list function than use print function foe print new list

if 4 in number:
    print("\nyes")
else :
    print("\nno")

print("\n1> append()")
number.append(10)                #Add only one element at the end of the List
character.append('g')
print(number.append(10))         #This statement return None value but also add the new element  
print(type(number.append(10)) )  #function in python is return 'None' data type, also add the new element 
print(number)
print(type(number))            # List data type        
print(character)

print("\n2> sort()")                #mix of str or int not allowed in sort()
number.sort()                    #sorts/arrange in ascending order by numbers in intiger
character.sort()                 #sorts/arrange in ascending order by alphabate in character
print(number.sort())
print(character)
print(number,"\n")

print("\n3> sort(reverse=True) ")   #mix of str or int not allowed in sort(reverse=True)
number.sort(reverse=True)        #sorts/arrange in Descending order by numbers in intiger
character.sort(reverse=True)     #sorts/arrange in Descending order by alphabate in character
print(number.sort())
print(character)
print(number)
                  
print("\n4> reverse()")
number.reverse()                # return reverses of the list(number)
print(number)                   # print reverses of the list
character.reverse()             # return reverses of the list(character)
print(character) 

print("\n5> insert(index no. , element)")
number.insert(8,11)            #insert element at giving index
print(number)
character.insert(8,11)
print(character)

print("\n6> remove(ele_val)")
number.remove(10)               # removes first occurrence of element
print(number)                  
character.remove('g')           # removes first occurrence of element
print(character) 

print("\n7> pop(index no.)")
number.pop(4)                # remove the element at 4th index number
print(number)
character.pop(4)             # remove the element from the 4th index number
print(character)


# number =[9,5,8,6,4,7,1,2,3]
# character =['f','a','e','b','d','c']

print("\n8> count(ele)")
print(number.count(9))      # count the how many time the number is present
print(character.count("f")) # count the how many time the number is present

print("\n9> copy( )")
a= number
a[0] = 0                    # that change in the list(number)
print(number)               # for save side we use copy method
a= number.copy()            # no change in number list only change in "a" list

# Tuples in Python

# A built-in data type that lets us create immutable sequences of values.

tup = (87, 64, 33, 95, 76) #tup[0], tup[1]..

# tup[0] = 43 #NOT allowed in python

tup1 = ( )

tup2 = ( 1, )    # tup2 =(1)   it is behave like ainteger data type

tup3 = ( 1, 2, 3 )



# Tuple Function in python
print("\nTuple Function in python")
tup = (1, 2, 3, 1)
print("element of tup")
print(tup)
# tup.index( element ) #returns index of first occurrence tup.index(1) is 0
print(tup.index(1))
# tup.count( element ) #counts total occurrences   tup.count(1) is 2
print(tup.count(1))