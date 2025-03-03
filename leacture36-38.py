# Error handling in python
# Error in Python can be of two types i.e. Syntax errors and Exceptions
# Errors are problems in a program due to which the program will stop the execution. 
# On the other hand, exceptions are raised when some internal events occur which change the normal flow of the program.

# Exceptions Error handling
a= (input("Enter the number "))
print (f"multiplication table of {a}")
# in the case of intput we type any thing
# But by the mistake we give wrong input so we face the error
# for the solution of the this type of problem we use
try:  
    for i in range (1 , 11):
        print(f"multiplication table of {a}= {a}*{i}=", (int (a)*i))
except:# at this place we can specifed the type of error so they stop can't terminate the code for some specific type of error
    print("Invalid Input")
    d=2*64
    print(d)
# we type wrong input so the interpter don`t show error print the code under except

try:  
    a=[1,4,7]
    print(a[5])
except IndexError:
    print("Invalid Index")

# finally clause

# it is a part of exception handling when we include a finally block at the end
# the finally block is always execuated 
# it generally used for doing the concluding task like closing file resource or closing excuaataion  

try:
    l = [2,5,'y','i','r']
    i = int(input("enter the index number "))
    print(l[i])
except:
    print("some error occur ")
    print(l)
finally:
    print("always execuated finally code")
# if you thing we use simple print at the place of finally
# but the print not work in all the places like function
# example:
def func():
    try:
        l = [2,5,'y','i','r']
        i = int(input("enter the index number "))
        print(l[i])
        return 1
    except:
        print("some error occur ")
        return 0
    finally:
        pass
    print("always execuated finally code") # this code of line not execuated
x=func()
print(x)
def func():
    try:
        l = [2,5,'y','i','r']
        i = int(input("enter the index number "))
        print(l[i])
        return 1
    except:
        print("some error occur ")
        return 0
    finally:
        print("always execuated finally code") # this code of line execuated now
x=func()
print(x)

# Rising custom error
# In python we create the error for some spical conoditions
# Rising error is depend on the user
#if the error is generate so the program is stoped
a= int(input("enter the value betweent the 1  to 10 "))
if (a<1 or a>10):
    print(a)
    raise ValueError("the value should not lie betweent the 1 to 10")
