import random 
num=random.randint(1,9)
chances=0


while chances<5:
    
    guess=int(input("enter any number between 1 to 9:"))
    break
if(guess == num):
    print("congrats you won")

if(guess>num):
    print("try once more this time,try a smaller number")

if(guess<num):
    print("try once more this time,try a bigger number")

if(chances==5):
    print("you lose !!!the correct number is=",num)

chances=chances+1


