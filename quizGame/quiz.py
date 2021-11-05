correct = "That is Correct!"
incorrect = "That is Incorrect"
score = 0
displayScore = "Your score is: "


print("Welcome to the Quiz Game!")
print("")
play = input("Do you want to play? ")
print("")
if play.casefold() != "yes":
    print("Goodbye")
    quit()

print("")

firstAnswer = input("What color is the sky? ")

print("")

if firstAnswer.casefold() == "blue":
    print(correct)
    score = score + 1
    print(displayScore, score)
    print("")
else:
    print(incorrect, "The correct answer is Blue")
    print("")

secondAnswer = input("What color is are fire truck usually? ")

if secondAnswer.casefold() == "red":
    print(correct)
    score = score + 1
    print(displayScore, score)
    print("")
else:
    print(incorrect, "The correct answer is Red")
    print("")


thirdAnswer = input("What is the solid form of water? ")

if thirdAnswer.casefold() == "ice":
    print(correct)
    score = score + 1
    print(displayScore, score)
    print("")
else:
    print(incorrect, "The correct answer is Ice")
    print("")


fourthAnswer = input("What is the color of the stars on the American flag? ")

if fourthAnswer.casefold() == "white":
    print(correct)
    score = score + 1
    print(displayScore, score)
    print("")
else:
    print(incorrect, "The correct answer is White")
    print("")


fourthAnswer = input("What state is famous for Hollywood? ")

if fourthAnswer.casefold() == "califonia":
    print(correct)
    score = score + 1
    print(displayScore, score)
    print("")
else:
    print(incorrect, "The correct answer is California")
    print("")

print("This is the end of the quiz! You scored", score, "Out of 5 questions. Great Job")