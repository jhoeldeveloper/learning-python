
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


# Dictionary = {key:value} unordered, changeable and indexed. No duplicate members

capitals = {"USA":"Washington D.C.",
            "UK":"London",
            "France":"Paris",
            "Germany":"Berlin"}

print(capitals["USA"])
print(capitals.get("USA"))

if capitals.get("Italy") == None:
    print("That capital does not exist")
else:
    print("That capital exists")

capitals.update({"USA":"WDC"})
capitals.update({"France":"ps"})
capitals.pop("UK")
capitals.popitem() # remove last item
#capitals.clear()
print(capitals.keys())

for key in capitals.keys():
    print(key)

print(capitals.values())

for value in capitals.values():
    print(value)

for key,value in capitals.items():
    print(f"{key}: {value}")


# Concession stand program

menu = {"hotdog":1.99,
        "hamburger":2.49,
        "fries":1.49,
        "soda":0.99,
        "water":0.49,
        "ice cream":1.99,
        "candy":0.99,
        "popcorn":1.49}

cart = []
total = 0

print("==== Menu ====")
for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        if food in menu:
            cart.append(food)
            total += menu[food]
        else:
            print("That food does not exist")

print(f"Total: ${total:.2f}")


# Random numbers

import random

options = ["rock","paper","scissors"]
cards = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

print(random.random())
print(random.randint(1,10)) # low and high
print(random.choice(options))
random.shuffle(cards)
print(cards)

# Number guessing game

import random

lowest = 1
highest = 10
answer = random.randint(lowest,highest)
guesses = 0
is_running = True

print(f"Guess a number between {lowest} and {highest}")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest or guess > highest:
            print("That number is not in the range")
            print(f"Guess a number between {lowest} and {highest}")
        elif guess < answer:
            print("TOO LOW")
        elif guess > answer:
            print("TOO HIGH")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"It took you {guesses} guesses")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Guess a number between {lowest} and {highest}")



# Rock, paper, scissors game

import random
options = ["rock","paper","scissors"]

running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter rock, paper or scissors: ").lower()

    print(f"Computer chose {computer}")
    print(f"you chose {player}")

    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "scissors":
        print("you win!")
    elif player == "scissors" and computer == "paper":
        print("you win!")
    elif player == "paper" and computer == "rock":
        print("you win!")
    else:
        print("you lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")


# Dice rolling game

import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘

"┌───────┐"
"│       │"
"│       │"
"│       │"
"└───────┘"

dice_art ={ 1: ["┌───────┐",
                "│       │",
                "│   ●   │",
                "│       │",
                "└───────┘"],
            2: ["┌───────┐",
                "│ ●     │",
                "│       │",
                "│     ● │",
                "└───────┘"],
            3: ["┌───────┐",
                "│ ●     │",
                "│   ●   │",
                "│     ● │",
                "└───────┘"],
            4: ["┌───────┐",
                "│ ●   ● │",
                "│       │",
                "│ ●   ● │",
                "└───────┘"],
            5: ["┌───────┐",
                "│ ●   ● │",
                "│   ●   │",
                "│ ●   ● │",
                "└───────┘"],
            6: ["┌───────┐",
                "│ ●   ● │",
                "│ ●   ● │",
                "│ ●   ● │",
                "└───────┘"]}
rolled_values = []
total = 0

attempts = int(input("How many dice would you like to roll?"))
for x in range(attempts):
    roll = random.randint(1,6)
    rolled_values.append(roll)

for value in range(5):
    for roll in rolled_values:
        print(dice_art[roll][value], end=" ")
    print()

for roll in rolled_values:
    total += roll

print(f"Total: {total}")



# functions - positional arguments

def display_invoice(username,amount,due_date):
    print(f"Hello {username}")
    print(f"Your invoice amount is {amount}")
    print(f"Please pay by {due_date}")

display_invoice("Neo",100,"01/01/2022")

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

print(add(5,3))
print(subtract(5,3))
print(multiply(5,3))
print(divide(5,3))


def create_name(first_name,last_name):
    return f"{first_name.capitalize()} {last_name.capitalize()}"

full_name = create_name("john","doe")
print(full_name)

# functions - default arguments

def net_price(list_price,discount=0,tax=0.05):
    return list_price * (1 - discount) * ( 1 + tax)

print(net_price(340))
print(net_price(340,0.1))
print(net_price(340,0.1,0.08))


import time
def count(end,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE")

count(10,5)


# functions - keyword arguments

def hello(greeting,title,first,last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello","Mr","John","Doe")
hello(title="Mr",first="John",last="Doe",greeting="Hello")

# functions - arbitrary arguments

def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(1,2,3,4,5,6,7,8,9,10))

def display_name(*names):
    for name in names:
        print(name, end=" ")

display_name("Dr.","john","jane","joe","jill")

def print_address(**kwargs): # dictionary
    for key,value in kwargs.items():
        print(f"{key}: {value}")

print_address(name="john",address="123 main st",city="new york",zip="10001")


def shipping_label(*args, **kwargs):
    for name in args:
        print(name, end=" ")
    print()
    for key,value in kwargs.items():
        print(f"{key}: {value}")

shipping_label("john","doe",address="123 main st",city="new york",zip="10001")


# Iterables

numbers = [1,2,3,4,5,6,7,8,9,10] # list

for num in reversed(numbers):
    print(num, end=" ")

print()

numbers = (1,2,3,4,5,6,7,8,9,10) # tuple

for num in reversed(numbers):
    print(num, end=" ")


print()

fruits = {"apple","orange","banana", "coconut"} # set

for fruit in fruits:
    print(fruit, end=" ")

print()

name = "john doe" # string

for letter in name:
    print(letter, end=" ")

print()

my_dictionary = {"name":"john","age":32,"city":"new york"} # dictionary

for key,value in my_dictionary.items():
    print(f"{key}: {value}")


# Membership operators

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter.upper() in word:
    print("Correct! The letter is in the word")
else:
    print("Incorrect! The letter is not in the word")


students = {"john","jane","joe","jill"} # set
student = input("Enter a student name: ")

if student in students:
    print(f"{student} was found in the class")
else:
    print(f"{student} was not found in the class")


grades = {"john":90,"jane":85,"joe":80,"jill":95} # dictionary
student = input("Enter a student name: ")

if student in grades:
    print(f"{student} has a grade of {grades[student]}")
else:
    print(f"{student} was not found in the class")


email = "joe@mail.com"

if "@" in email and "." in email:   
    print("Valid email address")
else:
    print("Invalid email address")


# list comprehension

doubles = [x * 2 for x in range(1,11)]
triples = [x * 3 for x in range(1,11)]
squares = [x ** 2 for x in range(1,11)]
print(doubles)
print(triples)
print(squares)


fruits = ["apple","orange","banana","coconut"]
upppercase_fruits = [fruit.upper() for fruit in fruits]
print(upppercase_fruits)


numbers = [1,-2,-3,4,5,6,-7,8,9,-10]
positive_numbers = [num for num in numbers if num > 0]
negative_numbers = [num for num in numbers if num < 0]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
print(positive_numbers)
print(negative_numbers)
print(even_numbers)
print(odd_numbers)


grades = [90,85,80,95,100,75,70,65,60]
passing_grades = [grade for grade in grades if grade >= 70]
print(passing_grades)

# Match-case (switch) statement

def day_of_week(day):
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Invalid day")

day_of_week(1)
day_of_week(4)

def is_weekend(day):
    match day:
        case 6 | 7:
            print("Weekend")
        case _:
            print("Weekday")

is_weekend(1)
is_weekend(7)