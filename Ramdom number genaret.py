print("Random number genaret")
import random

Cnumber = random.randrange(1, 101)
userInput = int(input("Enter the number : -"))
if userInput > Cnumber:
    print("Computer Number ", Cnumber)         
    print("your guess number is too high")
elif Cnumber > userInput:
    print("Computer number ", Cnumber)
    print("Your guess number is too Low")
else:
    print("Computer number ", Cnumber)
    print("Your number is equal")
