# The Walrus Operator in Python
# Allows you to assign a value to a variable within an expression.

# example 1
a=True
# a:=False :- first the assin the' a= False' then print the value of 'a'
print(a:=False)

# example 2
numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:
    print(numbers.pop())

# example 3
foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)