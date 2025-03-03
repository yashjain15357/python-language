import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# print(type(timestamp)) #time module return the data in string data type 
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(time.gmtime(0))
# print(time.time())

# this two way to presnt time with month and year


#One way to show time

print("\nway 1")
timr = time.ctime()
timr = timr.split()
print("Today day is :",timr[0])
print("present month is :".capitalize(),timr[1])
print("Today date is :",timr[2])
print("present time is :".capitalize(),timr[3])
print("Runing year is  :",timr[4])

# Another way to show time
from time import strftime
# strftime :- it return the time in a string form
#
print("\nway 2")
print("Today day is :",strftime("%a"))
print("present month is :".capitalize(),strftime("%b"))
print("Today date is :",strftime("%d"))
print("present time is :".capitalize(),strftime("%H:%M:%S"))
print("Runing year is  :",strftime("%Y"))
print("Runing time is  :",time.asctime())

# wishes code
from time import strftime
hour= int(time.strftime("%H"))
match hour:
    case _ if 6<=hour<=11:
        print("\nGood moorning sir ".upper())
    case _ if 17>=hour>=12:
        print("\nGood afternoon sir ".upper())
    case _ if 18<=hour<=20:
        print("\nGood evening sir ".upper())
    case _ if 21>=hour>=5:
        print("\nGood night sir ".upper())

print(time.localtime()[0])  #return according to index 
print(time.localtime())     #it return tuple and present time if the number of secound not pass in the localtime() function