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

answer = input("What color is the sky? ")

print("")

if answer.casefold() == "blue":
    print(correct)
    score += 1
    print(displayScore, score)
    print("")
else:
    print(incorrect, "The correct answer is Blue")
    print("")

answer = input("What color is are fire truck usually? ")

if answer.casefold() == "red":
    print(correct)
    score += 1
    print(displayScore, score)
    print("")
else:
    print(incorrect, "The correct answer is Red")
    print("")


answer = input("What is the solid form of water? ")

if answer.casefold() == "ice":
    print(correct)
    score += 1
    print(displayScore, score)
    print("")
else:
    print(incorrect, "The correct answer is Ice")
    print("")


answer = input("What is the color of the stars on the American flag? ")

if answer.casefold() == "white":
    print(correct)
    score += 1
    print(displayScore, score)
    print("")
else:
    print(incorrect, "The correct answer is White")
    print("")


answer = input("What state is famous for Hollywood? ")

if answer.casefold() == "califonia":
    print(correct)
    score += 1
    print(displayScore, score)
    print("")
else:
    print(incorrect, "The correct answer is California")
    print("")

print("This is the end of the quiz! You scored", score, "Out of 5 questions. Great Job")