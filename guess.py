import random
import math as m 

# Take lower limit and upper limit by the user
print("enter the game of the guess the number".upper())

lower = int(float(input("Enter the value of the lower limit ")))
upper = int(float(input("Enter the value of the upper limit ")))

# Generate random number and no of turns
ran = random.randint(lower , upper)
no_turn= int((m.sqrt(ran))+(m.cbrt(ran))-m.log(ran, 4))

print("You have a ",no_turn," number of turns")
# print(ran)
# print(id(ran))

gus= int(float(input(f"Gusse the number between {lower} to {upper} :")))
count = 1

while count <= no_turn:
    print(gus)
    temp = True

    while temp==True:
        try:
            if gus < lower or gus > upper:
                raise ValueError()
            
        except ValueError:
            print(ValueError("The number is not lie between the lower and upper"))
            gus= int(float(input(f"Gusse the number between {lower} to {upper} :")))

        if((gus >= lower) and (gus <= upper)):
            temp=False

    if gus < ran :
        print("This number is too small :")
        lower = gus
        gus= int(float(input(f"Gusse the number between {lower} to {upper} :")))
        # print(id(gus))

    elif gus > ran :
        print("This number is too big :")
        upper= gus
        gus= int(float(input(f"Gusse the number between {lower} to {upper} :")))
        # print(id(gus))
    elif gus is ran :
        print("congrulate you find the number".upper())
        break

    if count is no_turn: # 'is' key-word match the id of count and no_turn
        print("BETTER LUCK NEXT TIME")
        break

    count=count+1
