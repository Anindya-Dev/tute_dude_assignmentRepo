# Task 1: Calculate Factorial Using a Function 

# Problem Statement: Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output.

# n=int(input("Enter a number: "))
# def factorial(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)
# factorial(n)
# print(f"Factorial of {n} is : {factorial(n)}")

# Task 2: Using the Math Module for Calculations
 
# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)
# 3.   Displays the calculated results.

import math
x=int(input("Enter a number: "))
print(f"Square root: {math.sqrt(x)}")
print(f"Logarithm: {math.log(x)}")
print(f"Sine: {math.sin(x)}")