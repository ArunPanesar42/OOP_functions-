# What is Functions
# Why Functions

# how to create functions
# Syntax to create functions: "def" is the key word that tells the interpreter that the functions is being declared

# Lets Create a function
# Greeting function
# First iteration

# def greetings():    # If we run this program now there will be no outcome as we havent called it
#     print("Welcome on board.")
#
# greetings() #This calls the function

# # Second iteration takes the argument
# def greetings(name):
#     print("Welcome on board " + name)
# greetings("James")

# # Third iteration
# def add(num1, num2):    # This function passes 2 args and adds the two values
#     print(num1 + num2)
# add(3,6)

# # Fourth iteration - To use return statement instead of print()
# def subtract(num1, num2):
#     print("The numbers subtracted are") # this does print
#     return (num1 - num2) # This executes all computation but does not print
#     print("Your numbers subtracted are")   # This does not print because it is after the return, we need it before
# print(subtract(4,2))

# Create a calculator to add, subtract, divide, multiply
# display appropriate messages with the computation values as to what the outcome is from each funtion
# create a greeting function by taking user input as the user name and display it with the greeting message
name = input("Enter your name ")
num1 = int(input("Enter number 1 "))
num2 = int(input("Enter number 2 "))

def greet_user(name):
    print(f"Welcome {name}")

def add(num1, num2):
    print(" Your Numbers Added are:")
    print(num1 + num2)

def subtract(num1, num2):
    print(" Your Numbers subtracted are:")
    print(num1 - num2)

def multiply(num1, num2):
    print(" Your Numbers Multiplied are:")
    print(num1 * num2)

def divide(num1, num2):
    print(" Your Numbers divided are:")
    print(num1 / num2)

# calc = input("What calculation do you want to do")

greet_user(name)
add(num1, num2)
subtract(num1, num2)
multiply(num1, num2)
divide(num1, num2)


