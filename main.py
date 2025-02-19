
########################### Variables ###########################

# string

first_name = "Neo"
food = "pizza"
email = "neo@mail.com"

print(f"hello {first_name}")
print(f"you like {food}")
print(f"your email is {email}")

# Integer

age = 32
quantity = 3
num_students = 30

print(f"you are {age} years old")
print(f"you are buying {quantity} items")
print(f"your class has {num_students} students")

#  Float

price = 10.99
gpa = 3.2
distance = 5.5

print(f"the price is ${price}")
print(f"your gpa is {gpa}")
print(f"you ran {distance}km")

# Boolean

is_student = True

if is_student:
    print("you are a student")
else:
    print("you are NOT a student")



########################### Typecasting ###########################

name = "neo"
age = 32
gpa = 3.2
is_student = True


age = float(age)
gpa = int(gpa)
name = bool(name)


print(age)
print(gpa)
print(name)
print(type(gpa))

########################### input() ###########################


name = input("what is your name?: ")
age = int(input("how old are you?: "))

age = age + 1

print(f"hello {name}")
print(f"your age is {age}")

# exercise 1

length = int(input("Enter the length:"))
width = int(input("Enter the width:"))
area = length * width
print(f"The area is {area}")

# exercise 2

item = input("What item would you like to buy?:")
price = float(input("What is the price?:"))
quantity = int(input("How many would you like?:"))

total = price * quantity
print(f"you have bought {quantity} x {item}/s")
print(f"your total is {total}")

#exercise 3 - Madlibs game

adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, thing): ")
adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter a verb ending with 'ing: '")
adjective3 = input("Enter an adjective (desctiption)")

print(f"Today I went to a {adjective1} zoo.")
print(f"In a exhibit, i saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")

# Augmented assigment operators

friends = 5
friends += 1
print(friends)
friends -= 2
print(friends)
friends *= 3
print(friends)
friends /= 2
print(friends)
friends **= 2
print(friends)
friends %= 5
print(friends)

# Math related functions

x = 3.14
y = -4
z = 5

print(round(x)) #rounded value
print(abs(y)) #absoulute value
print(pow(4,3)) #4^3
print(max(x,y,z))
print(min(x,y,z))


import math

print(math.pi)
print(math.e)
print(math.sqrt(9))
print(math.ceil(9.9))
print(math.floor(9.9))

# Calculating circumference of a circle

import math
radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference is {round(circumference,2)} cm")

# calculating area of a circle

import math
radius = float(input("Enter the radius of a circle: "))
area = math.pi * pow(radius,2)
print(f"The area of the circle is: {round(area)}cm2")

# calculating Hipotenuse of a triangle

import math
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a,2) + pow(b,2))
print(f"Side C is {c}")

# conditional IF ELSE

age = int(input("Enter your age: "))
if age >= 100:
    print("you are too old to sign up!")
elif age >= 18:
    print("you are now signed up!")
elif age < 0:
    print("you haven't been born yet!")
else:
    print("you must be 18+ to sign up")



response = input("Would you like food? (Y/N): ")
if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")



name = input("Enter your name: ")
if name == "":
    print("you did not type in your name!")
else:
    print(f"Hello {name}")


for_sale = True
if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale ")

# Python calculator

operator = input("Enter an operator(+ - * /):")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1/num2)
else:
    print(f"{operator} is not valid operator")

# Python weight converter

weight = float(input("Enter you weight:"))
unit = input("kilograms or pounds? (K or L):")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"your weight is {round(weight,1)} {unit}")
if unit == "L ":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"your weight is {round(weight,1)} {unit}")
else:
    print(f"{unit} was not valid")

# Python temperature converter

unit = input("Is this temperature in celsius or fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32,1)
    print(f"The temperature in farenheit: {temp} F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in celsius: {temp} C")
else:
    print(f"{unit} is a invalid unit of measurement")


# Logical operators

temp = 25
is_raining = True
is_sunny = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")

if temp >= 28 and not is_sunny:
    print("It is HOT outside")
    print("It is NOT SUNNY")

# Conditional expressions

num = 5
a = 6
b = 7
age = 14
temperature = 30
user_role = "admin"

print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

max_num = a if a > b else b
min_num = a if a < b else b
print(f"max:{max_num}, min:{min_num}")

status = "Adult" if age >= 18 else "Child"
print(status)

weather = "HOT" if temperature > 20 else "COLD"
print(weather)

access_level = "Full Access" if user_role == "admin" else "Limited access"
print(access_level)


# String methods

name = input("Enter your full name: ")
phone_number = input("Enter your phone number: ")

result = len(name)
print(result)
print(name.find("o")) # return the index of first ocurrence
print(name.rfind("o")) # return the index of last ocurrence
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit()) # only numbers
print(name.isalpha()) # only alphabetic
print(phone_number.count("8"))
print(phone_number.replace("-", ""))
print(help(str))


# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not cointain spaces
# 3. username must not contain digits 

username = input("Enter a username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")


# Indexing string [start:end:step]

credit_number = "1234-5678-9012-3456"
print(credit_number[0])
print(credit_number[:4]) # [0:4] = [:4]
print(credit_number[5:9])
print(credit_number[5:]) # from 5 to last index
print(credit_number[-3])
print(credit_number[::3])
print(f"XXXX-XXXX-XXXX-{credit_number[-4:]}")
print(credit_number[::-1]) # reverse string


# Format specifiers {value:flags}

price1 = 3.14159
price2 = -3943.45
price3 = 2153.4644

print(f"Price 1 is {price1:.2f}") # 2 decimals
print(f"Price 2 is {price2:10}")
print(f"Price 3 is {price3:010}")

print(f"Price 1 is {price1:>10}") # align right
print(f"Price 2 is {price2:<10}") # align left
print(f"Price 3 is {price3:^10}") # align center

print(f"Price 1 is {price1:+}") # add + positive numbers
print(f"Price 2 is {price2:,}") # add , large numbers
print(f"Price 3 is {price3:+,.2f}") # align center


# while loop

name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")

print(f"Hello {name}")


food = input("Enter a food you like (q to quit): ")
while not food == "q":
    print(f"you like {food}")
    food = input("Enter a food you like (q to quit): ")

print("bye")


num = int(input("Enter a # between 1 - 10"))
while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"your number is {num}")


#Python compound interest calculator

principle = 0 
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle amount can't be less than 0")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than 0")
    else:
        break

while True:
    time = float(input("Enter the time: "))
    if time < 0:
        print("time can't be less than 0")
    else:
        break


total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} years is {total:.2f}")


# for loops

for x in range(1,11):
    print(x)

for x in reversed(range(1,11)):
    print(x)

for x in range(1,11,2): #(start,end,step)
    print(x)

credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)

for x in range(1,21):
    if x == 13:
        continue # skip 13
    else:
        print(x)

for x in range(1,21):
    if x == 13:
        break # stop at 13
    else:
        print(x)



# Python countdown timer

import time
my_time = int(input("Enter the time in seconds: "))
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")

# Nested loops

for x in range(3):
    for y in range(1,10):
        print(y, end="")
    print()

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()


# Collections

# List = [] ordered and changagle. Allows duplicate members

fruits = ["apple","orange","banana", "coconut"]

print(fruits[::-1])

for fruit in fruits:
    print(fruit)

print(len(fruits))
print("banana" in fruits)

fruits[0] = "pineapple"
print(fruits)

fruits.append("kiwi")
print(fruits)

fruits.remove("orange")
print(fruits)

fruits.insert(1,"cherry")
print(fruits)

fruits.sort()
fruits.reverse()

print(fruits.index("kiwi"))
print(fruits.count("kiwi"))

print(fruits)

#fruits.clear()

#print(dir(fruits))
#print(help(fruits))


# set = {} unordered and immutable. No duplicate members


fruits = {"apple","orange","banana", "coconut"}
print(len(fruits))
print("banana" in fruits)
fruits.add("kiwi")
fruits.remove("orange")
fruits.pop()
#fruits.clear()
print(fruits)


# Tuple = () ordered and unchangagle. Allows duplicate members. FASTER

fruits = ("apple","orange","banana", "coconut")
print(len(fruits))
print("banana" in fruits)
print(fruits.index("banana"))
print(fruits.count("banana"))
for fruit in fruits:
    print(fruit)




# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input("Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("==== Shopping Cart ====")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print(f"\nTotal: ${total:.2f}")


# two dimensional list

fruits = ["apple","orange","banana", "coconut"]
vegetables = ["carrot","broccoli","spinach","kale"]
meats = ["beef","chicken","pork","lamb"]

groceries = [fruits,vegetables,meats]


for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()


# Two dimensional keeypad

num_pad = ((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))

for row in num_pad:
    for key in row:
        print(key, end=" ")
    print()

# Python quiz game

questions = ("How many elements are in the periodic table?",
            "Which animal lays the largest eggs?",
            "What is the most abundant gas in the Earth's atmosphere?",
            "How many bones are in the human body?",
            "Which planet in the solar system is the hottest?")

options = (("A.116","B.117","C.118","D.119"),
            ("A.Whale","B.Crocodile","C.Elephant","D.Ostrich"),
            ("A.Nitrogen","B.Oxigen","C.Carbon-Dioxide","D.Hydrogen"),
            ("A.206","B.207","C.208","D.209"),
            ("A.Mercury","B.Venus","C.Earth","D.Mars"))

answers = ("C","D","A","B","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("(------------------)")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter your guess: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer is {answers[question_num]}")

    question_num += 1

score = (score / len(questions)) * 100
print(f"Your score is {score:.2f}%")
