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