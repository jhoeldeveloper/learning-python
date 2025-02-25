
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


# modules

#import math
import math as m
from math import pi

print(m.pi)
print(pi)



# Varibble scope - scope resolution
# Local, Enclosing, Global, Built-in


def func1():
    x = 1 # local
    print(x)

def func2():
    x = 2 # local
    print(x)

func1()
func2()

def func3():
    x = 3 # enclosed
    def func4():
        print(x) # enclosed
    func4()

func3()

x = 4 # global
def func5():
    print(x) # global

def func6():
    print(x) # global

func5()
func6()

from math import e

def func7():
    print(e) # built-in

e = 3

func7()


# special variable __name__

def my_function(x):
    return x * 2

def another_function(y):
    return y + 1

if __name__ == "__main__":
    result1 = my_function(5)
    result2 = another_function(10)
    print(f"Test results: {result1}, {result2}")


# Banking program

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to deposit: "))
    if amount <= 0:
        print("Invalid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds")
    elif amount <= 0:
        print("Invalid amount")
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking program")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit(balance)
            show_balance()
        elif choice == "3":
            balance -=withdraw(balance)
            show_balance()
        elif choice == "4":
            is_running = False
        else:
            print("Invalid choice")

    print("Thank you have a nice day!")

if __name__ == "__main__":
    main()

# Slot machine program

import random

def spin_row():
    import random
    symbols = ["🍒","🍋","🍉","🔔","⭐"]
    return [random.choice(symbols) for x in range(3)]

def print_row(row):
    print("****************")
    print(" | ".join(row))
    print("****************")

def get_payout(row,bet):
    payout = 0
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            payout = bet * 3
        elif row[0] == "🍋":
            payout = bet * 5
        elif row[0] == "🍉":
            payout = bet * 10
        elif row[0] == "🔔":
            payout = bet * 20
        elif row[0] == "⭐":
            payout = bet * 50
    return payout

def main():
    balance = 100
    print("********************************")
    print("Symbols: 🍒 🍋 🍉 🔔 ⭐")
    print("********************************")

    while balance > 0:
        print(f"Your balance is ${balance}")
        bet = input("Enter your bet: ")
        if bet.isdigit():
            bet = int(bet)
            if bet > balance:
                print("Insufficient funds")
            elif bet <= 0:
                print("Invalid bet")
            else:
                balance -= bet
                row = spin_row()
                print_row(row)

                payout = get_payout(row,bet)

                if payout > 0:
                    balance += payout
                    print(f"Congratulations! You won ${payout}")
                else:
                    print("Better luck next time")

main()


# Encryption program

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

plain_text = input("Enter a message to encrypt: ")
encrypted_text = ""

for letter in plain_text:
    index = chars.index(letter)
    encrypted_text += key[index]
    
print(f"Original message: {plain_text}")
print(f"Encrypted message: {encrypted_text}")

print("****** reverse *******")

encrypted_text = input(f"Enter a message to decrypt ({encrypted_text}): ")
decrypt_text = ""

for letter in encrypted_text:
    index = key.index(letter)
    decrypt_text += chars[index]
    
print(f"Encrypted message: {encrypted_text}")
print(f"Decrypted message: {decrypt_text}")


# Hangman game

import random

words = ("apple","banana","cherry","elderberry","lemon","mango","orange","papaya","raspberry","strawberry","watermelon")
hangman_art = ["_______",
            "|     |",
            "|     O",
            "|    /|\\",
            "|    / \\",
            "|"]

def display_man(wrong_guesses):
    print("******************")
    for line in hangman_art[:wrong_guesses]:
        print(line)
    print("******************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = ()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()
        if len(guess) > 1 or not guess.isalpha():
            print("Invalid input")
            continue
        if guess in guessed_letters:
            print(f"{guess} is already guessed")

        if guess in answer:
            for index in range(len(answer)):
                if answer[index] == guess:
                    hint[index] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False

main()


# Object oriented programming

class Car:
    def __init__(self,model,year,color,for_sale):
        self.model = model
        self.color = color
        self.year = year
        self.for_sale = for_sale
    def drive (self):
        print(f"you drive the {self.color} {self.model}")

    def stop(self):
        print(f"you stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")


car1 = Car("Mustang",2024,"red",False)
car2 = Car("Corvette",2025,"blue",False)
car3 = Car("Charger",2024,"yellow",True)

print(car1.model)
print(car2.color)
print(car3.year)
car1.drive()
car2.stop()
car1.describe()


# classes

class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("jon",20)
student2 = Student("jane",34)
student3 = Student("sandy",35)
student4 = Student("nia",33)

print(student1.name)
print(student1.age)
print(student1.class_year)
print(student1.num_students)


# Inheritance

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
   def speak(self):
        print("SQUEEK!")


dog = Dog("Scooby doo")
cat = Cat("Garfield")
mouse = Mouse("Mickey")


print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()



# Multiple inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()

rabbit.eat()
hawk.sleep()
fish.eat()


# Super function

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color,filled)
        self.radius = radius
    
    def describe(self):
        super().describe()
        print(f"It is circle with an area of {3.14 * self.radius * self.radius} cm2")


class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color,filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color,filled)
        self.width = width
        self.height = height


circle = Circle("red", True, 4)
square = Square(color="blue",filled=True,width=5)
print(circle.color, circle.filled)
print(square.color, square.filled)

circle.describe()


# Polimorphism => Poly = many; Morphe = form
# Inheritance

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side ** 2
        
class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    
    def area(self):
        return self.base * self.height * 0.5

class Pizza(Circle):
    def __init__(self,topping,radius):
        super().__init__(radius)
        self.topping = topping
        

shapes = [Circle(4), Square(5), Triangle(6,7),Pizza("pepperoni", 15)]

for item in shapes:
    print(f"{item.area()}cm2")


# Polimorphism => Poly = many; Morphe = form
# Duck typing => "If it look like a duck and quacks like a duck, it must be a duck"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car():
    alive = False
    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)



# Static methods = A method that belongs to a class rather than any object from that class(instance)
# Usually used for general utility functions

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions


employee1 = Employee("Eugune","Manager")
employee2 = Employee("Squidward","Cashier")
employee3 = Employee("Spongebob","Cook")


print(Employee.is_valid_position("Rocket scientist"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())


# Class methods

class Student:
    count = 0
    total_gpa = 0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_gount(cls):
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa/cls.count:.2f}"

student1 = Student("Spongebob",3.2)
student2 = Student("Patrick",3.2)
student3 = Student("Sandy",4.0)

print(Student.get_gount())
print(Student.get_average_gpa())


# Magic methods

class Book:
    def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self,other):
        return self.num_pages < other.num_pages
    
    def __gt__(self,other):
        return self.num_pages > other.num_pages
    
    def __add__(self,other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self,key):
        if key == "title":
            return self.title
        if key == "author":
            return self.author
        if key == "num_pages":
            return self.num_pages
        else:
            return f"Key {key} was not found"
    

book0 = Book("The Hobbit","J.R.R. Tolkien", 310)
book1 = Book("The Hobbit","J.R.R. Tolkien Jr.", 310)
book2 = Book("Harry Potter and the Philosopher's stone","J.K. Rowling", 223)
book3 = Book("The Lion, the witch and the wardrobe","C.S. Lewis", 172)

print(book1)
print(book0 == book1)
print(book2 < book1)
print(book2 > book1)
print(book2 + book1)
print("Lion" in book3)
print(book3["title"])
print(book3["author"])
print(book3["num_pages"])
print(book3["rate"])


# @property => add aditional logic when read, write, or delete attributes

class Rectangle:
    def __init__(self,width,height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f} cm"

    @property
    def height(self):
        return f"{self._height:.1f} cm"

    @width.setter
    def width(self,new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self,new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")


rectangle = Rectangle(3,4)

rectangle.width = -2
rectangle.height = 4

# del rectangle.width
# del rectangle.height

print(rectangle.width)
print(rectangle.height)



# Decorator => a function that extends the bahavior of another function

def add_sprinkles(func):
    def wrapper(*args,**kwargs):
        print("*you add sprinkle 🎊*")
        func(*args,**kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args,**kwargs):
        print("*you add fudge 🍫*")
        func(*args,**kwargs)
    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍨")

get_ice_cream("vanilla")



# Exception => an event that interrupts the flow of a program


try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Enter only number please.")


try:
    number = int(input("Enter a number: "))
    print(1/number)
except Exception:
    print("something went wrong")
finally:
    print("Do some cleanup here")


# File detection

import os

file_path = "files/file.txt"
file_path2 = "C:\\Users\\User\\Desktop"


if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("The location doesn't exist")

# writting files

txt_data = "I like pizza!"
file_path = "output.txt"

with open(file=file_path, mode="w") as file: # mode x if file existes, mode a for append content 
    file.write(txt_data)
    print(f"txt file {file_path} was created")

employees = ["Eugene","Squidward","Spongebob","Patrick","Sandy"]

try:
    with open(file_path,"w") as file:
        for employee in employees:
            file.write(employee + "\n")
        print(f"txt file {file_path} was created")
except FileExistsError:
    print("That file already exists")

#writing json
import json
employees = {"name":"Spongebob","age":30,"job":"cook"}

try:
    with open(file_path,"w") as file:
        json.dump(employees,file, indent=4)
        print(f"txt file {file_path} was created")
except FileExistsError:
    print("That file already exists")

# writing csv
import csv
employees = [["Name","Age","Job"],
             ["Spongebob",30,"Cook"],
             ["Patrick",34,"Unemployed"],
             ["Sandy",25,"Scientist"]]

try:
    with open(file_path,"w",newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"txt file {file_path} was created")
except FileExistsError:
    print("That file already exists")


# Reading files
import json
import csv
file_path = "output.txt"

try:
    with open(file_path,"r") as file:
        #content = file.read()
        #content = json.load(file)
        content = csv.reader(file)
        for line in content:
            print(f"{line[0]},{line[1]}")
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")


# Date and time

import datetime

date = datetime.date(2025,1,2)
date = datetime.date.today()
time = datetime.time(12,30,0)
time = datetime.datetime.now()
time = time.strftime("%H:%M:%S %d/%m/%Y")

target_datetime = datetime.datetime(2030,1,2,12,30,0)
current_datetime = datetime.datetime.now()

print(date)
print(time)


if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date hasn't passed yet")


# Alarm clock

import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarma set for {alarm_time}")
    sound_file = "BuilttoLast.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP!😫")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running = False
        time.sleep(1)


alarm_time = input("Enter the alarm time (HH:MM:SS)")
set_alarm(alarm_time)


# Multithreading 

import threading 
import time

def walk_dog(first,last):
    time.sleep(8)
    print(f"you finish walking the {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("you take out the trash")

def get_mail():
    time.sleep(4)
    print("you get the mail")


chore1 = threading.Thread(target=walk_dog, args=("Scooby","Doo"))
chore1.start()
chore2 = threading.Thread(target=take_out_trash)
chore2.start()
chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chore are complete")


# How to connect to an API 

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemon_name = "mew"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name']}")
    print(f"Id: {pokemon_info['id']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")