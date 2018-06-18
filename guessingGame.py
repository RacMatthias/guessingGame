import random

value = random.randint(0,101)   #create random number between 0 and 100
tryCounter = 1

print ("***Guess the number!***")

userInput = int(input("Guess: "))    #request a guess from user

while value != userInput:   #check if user gut the number
    print ("***Sorry wrong number. Guess again!**")
    tryCounter += 1     #increment tryCounter by 1

    if userInput < value:   #give hints to the user
        print("**You number is too small!**")
    else:
        print("**You number is too big!**")

    userInput = int(input("Input: "))   #lets user guess again
else:
    print("***You got it!***")
    print("You needed", tryCounter, "trys.")
