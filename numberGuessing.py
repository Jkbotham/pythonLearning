import random

print("Welcome to the Number Guessing Game! Good Luck")
print()

x = int(input("How big of range should we use? "))

number = random.randint(1,x)

def question(): 
    guess = input("Guess a number between 1 and " + str(x) + "! ")

    if int(guess) > x:
        print("That guess is not within the range. Guess a number between 1 and " + str(x) + "! ")
        print()
        question()

    if int(guess) != number: 
        print("That is incorrect")
        print()
        question()
    else:
        print("Thats correct! The number is " + str(number) + "!")
        quit()

question()
