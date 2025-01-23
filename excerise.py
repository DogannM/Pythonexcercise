#Beginner-Level Exercises
#Hello, World!
print("hello, world!")
#Write a program that prints "Hello, World!" to the screen.
print("hello, world!")
#Modify it to ask for the user's name and greet them.
greetings = input("What is your name? :")
print("Greetings, " + greetings + "!") 

#Simple Arithmetic
#Create a program that takes two numbers from the user and performs addition, subtraction, multiplication, and division.
var1 = ""
var2 = ""

while not var1.isdigit():
    var1 = input("Enter a number: ")
    if not var1.isdigit():
        print("Invalid input. Please enter a number.")

while not var2.isdigit():
    var2 = input("Enter another number: ")
    if not var2.isdigit():
        print("Invalid input. Please enter a number.")
        
var1 = int(var1)
var2 = int(var2)

if var1 == 0 or var2 == 0:
    print("You cannot enter 0 !!")
    if var1 == 0:
        var1 = input("Enter a number other than 0: ")
        var1 = int(var1)
    if var2 == 0:
        var2 = input("Enter a number other than 0: ")
        if var2.isdigit():
            var2 = int(var2)

print("Addition: " + str(var1 + var2))
print("Subtraction: " + str(var1 - var2))
print("Multiplication: " + str(var1 * var2))
print("Division: " + str(var1 / var2))

#Odd or Even
#Write a program that asks the user for a number and prints whether it is odd or even.

#Basic Calculator
#Create a calculator that performs basic operations (add, subtract, multiply, divide) based on user input.


#Guess the Number
#Generate a random number between 1 and 100 and let the user guess it, giving hints (higher/lower) until they get it right.
