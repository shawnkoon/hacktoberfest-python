# importing random to make use of it for tuples
import random

print("Hello World")

# Closes Issue: #9
# Asks the user to enter their name and displays it to them
userName = input("Enter your name: ")
print("Hello %s!" % userName)

# Closes Issue: #8
# Picks a random fruit from the tuple and tells the user to eat it
fruits = ("apple", "banana", "cherry", "strawberry", "pineapple", "mango",
          "grape", "orange")
print("You should eat a %s." % fruits[random.randint(0, len(fruits))])

# Closes Issue: #6
# Creates an array of car names
cars = ["Ford", "Toyota", "Honda", "Mazda", "Tesla", "BMW"]

# Closes Issue: #4
# Will make use of arithmetic operations by trying to guess the user's age
print("The computer will guess your age.")
age = int(input("Pick a number between 1 and 10: "))
age = ((age * 2) + 5) * 50
passed = input("Has your birthday already passed (Y/N): ")
if passed == "Y":
    age += 1768
elif passed == "N":
    age += 1767
year = int(input("What year were you born in: "))
age = age - year
newAge = str(age)
print("You are %s years old." % newAge[-2:])
