#  Task 1: Perform Basic Mathematical Operations
# Problem Statement: Write a Python program that does the following:
# 1.  Takes two numbers as input from the user.
# 2.  Performs the basic mathematical operations on these two numbers:
# o	Addition
# o	Subtraction
# o	Multiplication
# o	Division
# 3.  Displays the results of each operation on the screen.

x=int(input("Enter the first number: "))
y=(int(input("Enter the second number: ")))
print("Addition: ",x+y)
print("Subsraction: ",x-y)
print("Multiplication: ",x*y)
print("Division: ",x/y)

# Task 2: Create a Personalized Greeting
# Problem Statement: Write a Python program that:
# 1.  Takes a user's first name and last name as input.
# 2.  Concatenates the first name and last name into a full name.
# 3.  Prints a personalized greeting message using the full name.

a=input("Enter you first name: ")
b=input("Enter you last name: ")
print(f"Hello, {a} {b}! Welcome to Python Program.")
