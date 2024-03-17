import random
import sys
while (True):
    x=int(input("Enter the starting number: "))
    y=int(input("Enter the ending number: "))
    compclc=random.randrange(x,y)
    while (True):
        userclc=str(input("Guess the number or to quit press q: "))
        if (userclc)==str(compclc):
            print("You guessed the number correctly")
            break
        else:
            if(userclc=="q"):
                sys.exit()
            else:
                continue
    againpl=input("Do you wanna play? Y/N : ")
    if againpl=="Y":
        continue
    else:
        sys.exit()