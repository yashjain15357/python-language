#LEACTURE 5 LOOPS
# loop are used to repeat instruction 

#  WHILE LOOPS
"""
variable initialization before the use in a loop_stop_condition
`SYANTAX OF WHILE LOOP`
while_loop_stop_condition_:
    code.....
    "update value of variable for gaining loop_stop_condition"

"""
# example of while loop
loop_stop_condition=1
while loop_stop_condition<=5:
    print("hii my crush")
    loop_stop_condition+=1 
print(loop_stop_condition)  
# print the element of list
# this is example of `traverse`
# traverse mean :- go the element of list/tuple one by one and perform some action/print the element is called traverse
num=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(num):
    print(num[i])
    i+=1

# Break,Continue statement

"""
Break Statement in Python
The break statement in Python is used to terminate the loop or statement in which it is present. 
After that, the control will pass to the statements that are present after the break statement, if available. 
If the break statement is present in the nested loop, then it terminates only those loops which contain the break statement.
"""
s='geeksforgeeks'
while True: 
    print(s[i]) 
  
    # break the loop as soon it sees 'e' 
    # or 's' 
    if s[i] == 'e' or s[i] == 's': 
        break
    i += 1
  
print("Out of while loop")

"""
Continue Statement in Python
When the continue statement is executed in the loop,
the code inside the loop following the continue statement will be skipped and 
the next iteration of the loop will begin.
"""
j=0
s='geeksforgeeks'
while j<13:
    if s[j] == 'e' or s[j] == 's': 
        j+=1
        continue 
        
    print(s[j]) 
    j += 1 
print("Out of while loop")   

# FOR LOOP in python 
"""
Python For loop is used for sequential traversal i.e. 
it is used for iterating over an iterable like String, Tuple, List, Set, or Dictionary.
"""
    
# Python Program to 
# show range() basics 

# printing a number (start with 0 end up to (stop condition - 1))
for i in range(10):                       # (10) is a stop condition 
	print(i, end=" ") 

# performing sum of first 10 numbers 
sum = 0
for i in range(1, 10):                    #(1) is a start condition (10) is a stop condition work up to (n-1)
	sum = sum + i 
print("\nSum of first 10 numbers :", sum)
# his code uses the zip() function to iterate over two lists (fruits and colors) in parallel. 
# The for loop assigns the corresponding elements of both lists to the variables fruit and color in each iteration.
fruits = ["apple", "banana", "cherry"] 
colors = ["red", "yellow", "green"] 
for fruit, color in zip(fruits, colors): 
	print(fruit, "is", color) 
     
# loop with else 

for i in range(5):
     print("iteration no. {} in for loop ".format(i+1))
else:
     print("else in loop")
print ("out of the loop ")

for i in range(7):
     print(i)
     if (i==4):
          break
else:        #  this else come under the loop so after the break yash not print
     print("yash")
print("0000000000000000000000000000000000000000000000")
# Enumerate function in python 
num = [15,16,86,94,3,689,3,76,]
# basic way of print element of index number
# index = 0 
# for num in num:
#      print (num )
#      if (index == 3):
#           print("i hate you ")
#      index += 1
# new way for print index number
for index ,j in enumerate (num , start = 1): # start = 1 mean the index start with the number 1
    print (j , index)                   # index stored the index number and j stored the value of the list
    if (index == 3):
          print("i hate you ")
    index += 1


