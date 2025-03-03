# Map filter and reduce 
# In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements 
# and return a new sequence.

# Map
''' 
# The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements. 
# map(function, iterable) # syntax of map function
# iterable sequential data type of python go in the function block
# and return the the output of all element are update according to the function block
 the map return the map type''' 

# function :- any function or command  
def cube(a):
    return a**3
# List of numbers
numbers = [1, 2, 3, 4, 5]
# Double each number using the map function
doubled = map(cube, numbers)
# Print the doubled numbers
print(list(doubled))

# filter function
'''
the filter function filters a sequence of elements based on a given predicate 
(a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate. 
The filter function has the following syntax:

filter(predicate, iterable)

The predicate argument is a function that returns a boolean value 
and is applied to each element in the iterable argument. 
The iterable argument can be a list, tuple, or any other iterable object.'''

# function :- any function or command  
def even(x):
     return x % 2 == 0 # this condition is true so is accept
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Get only the even numbers using the filter function
evens = filter(even, numbers)
# evens = filter(lambda x: x % 2 == 0, numbers) # we use this against of the uper line
# Print the even numbers
print(list(evens))
# reduce
'''
The reduce function is a higher-order function that applies a function to a sequence and 
returns a single value. It is a part of the functools module in Python and has the following syntax:

reduce(function, iterable)

The reduce function applies the function to the first two elements in the iterable 
and then applies the function to the result and the next element, and so on. 
The reduce function returns the final result.
'''

from functools import reduce
# List of numbers
numbers = [1, 2, 3, 4, 5]
# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)
# Print the sum
print(sum) 
