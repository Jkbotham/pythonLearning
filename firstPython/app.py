# msg ="Hi James!!"
# whoops= 4444
# birthYear = input("Whats your birth year? ")


# age = 2021 - int(birthYear)


# first = float(input("First number to be entered "))
# second = float(input("Second number to be entered "))
# whoops = input("What function are we doing? ")


# answer = first + second;

# print("Sum: ", answer);


# int() Makes a string a integer
# float() something to do with numbers with decmail places
# bool() Converting a string to a Boolean
# str() Coverting a number to a string


# print(msg.casefold())
# print(msg.find("J"))
# msgLower = msg.casefold()
# name = "JameS"
# print(name.casefold())
# replace = msgLower.replace(name.casefold(), "billy")
# print(replace)


# expression = 3 == 2
# print (expression)

# price = 10.1

# print(price > 10 and price < 30)
# print(price > 10 or price < 30)
# print(not price > 10)

# temp = 21

# if temp > 30:
#     print("Its hotter than 30 degrees")
#     print("feels pretty hot outside")
# elif temp > 20:
#     print("cold out there boys")
# else:
#     print("yeah tis cold")


# weight = float(input("What is your weight? "))
# kOrL = input("(K)g or (L)bs ")

# if kOrL.casefold() == "l":
#     print("You weigh ", weight / 2.2046, "KG")
# elif kOrL.casefold() == "k":
#     print("You weigh ", weight * 2.046), "LBS"



# ------------------------------------------------------------

name = "James"

#Length of name
print(len(name))

#Finds the index of a in string
print(name.find("a"))

# Capitalizes first char in string
print(name.capitalize())

# # Capitalizes all char in string
print(name.upper())

# Lower cases' all char in a string
print(name.lower())

# Checks if name is a digit
print(name.isdigit())

# Checks if name is all alphabetic chars
print(name.isalpha())

# Counts number of specific char in a string
print(name.count("J"))

# Replaces one char with another
print(name.replace("J","U"))

#Multiples the string to display X times
print(name*3)

# ----------------------------------------------

# Math Functions

import math

pi = 3.14
x=1
y=2
z=3


# Rounds number for us
print(round(pi))

# Rounds number UP.. Math ceiling
print(math.ceil(pi))

# Rounds down
print(math.floor(pi))

# Absolute value of a number
print(abs(pi))

# Raise a base number to a power
print(pow(pi, 2))

# Square root funtion
print(math.sqrt(pi))

# Largest of a varying amount of values
print(max(x,y,z))

# Find lowest value 
print(min(x,y,z))

# --------------------------------------------------

# String slicing
# Use either indexing[start:stop:step] or slice()

name = "James Botham"

# Creating substring based off portion of my name
firstName = name[0:5]
lastName = name[6:]
funkyName = name[0:12:2]
# Reverse Name
reversedName = name[::-1]

print(firstName)
print(lastName)
# Displays every second char
print(funkyName)
print(reversedName)

# Slice Function

website = "http://google.com"

slice = slice(7,-4)

print(website[slice])

# --------------------------------------------------

# Logical Operators [and, or, not]
# if not(temp >=0 and temp <=30:)

# --------------------------------------------------

# for loops

# for i in range(10):
#     print(i+1)

# Counts each number bettween the given range.  range(start number, end number, step)
for i in range (100, 50-1,-1):
    print(i)

# Prints each letter in the string
for i in "James Botham":
    print(i)

import time

# for seconds in range(10,0,-1):
#     print(seconds)
    # This pauses for one second in each iteration of the loop
    # time.sleep(1)
# Once the 10 second loop is finished above it runs the print below
print("Happy New Year")

# Difference bettwen for and while loops:  A for loop will execute a limited amount of time and a while loop will execute for an unlimited amount of time untill given and escape command.


# --------------------------------------------------

# Nested loops -- One loop inside another loop: The "inner loop" will finish all iterations before finishing one iteration of the "outter loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        # print(columns)
        # This end="" will prevent the print from going down to a new line.
        print(symbol, end="")
    print()
