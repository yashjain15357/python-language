print("# #average of three no.")
def average(a,b,c):
    print("the numbers is",a,b,c)
    return (a+b+c)/3

avg=average(1,2,3)    
average(1,2,3)
print(avg)



# def list(a,b ):
#     print(a[3])
#     print(b[3])

# list([2,3,8,3,4,6],['a','b','c','d','e'])

print("factorial function")

def fac(a):
    sum =1
    for v in range(1,a+1):
        sum =sum*v
    print("the factorial value is ",end="")
    return(sum)
# def fac(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fac(n - 1)
if __name__ == "__main__":
    fac(5)
# doller too indian ruppes 
# 1 doller = 83 rupees
# def vol(v):
#     print("your doller price is : ",v)
#     # a=input()
#     print("your indian rupees is ", (v*83))
# a=int(input("enter the value of a "))
# vol(a)

# recursion in the python language 
# def rec(a):
#     if(a==0):
#         return 0
#     print(a)
#     rec(a-1)       #this is stored 2 time 
#     print("yash")  #this is print 3 time 
# rec(3)

# def fact (n):
#     if ((n==0)or(n==1)):
#         return 1
#     else:
#         return n+(fact(n-1))
# number =int(input("the number is :"))
# print(fact(number))


# Write a recursive function to print all elements in a list.
# def prin(a):
#     if (len(a)==0):
#         return 0
#     print(a[len(a-1)])


# a=[2,3,8,3,4,6]
# print(prin(a))
print("sum")
def sum():
    a = 12
    b=12
    return (a+b)
if __name__ == "__main__":
    c=sum()
    print(c)











