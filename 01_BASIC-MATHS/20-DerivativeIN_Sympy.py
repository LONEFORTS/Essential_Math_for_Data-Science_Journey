# Hello World... 6:48 PM 
#date:| 30 July 2026 | Thursday

# Importing everything from the SymPy library (used for symbolic mathematics)
from sympy import *

# Create a symbolic variable named 'x'
# This tells SymPy that x is a mathematical variable, not a normal Python variable.
x = symbols('x')

# Define the mathematical function:
# f(x) = x²
f = x**2

# Find the derivative (formula for the steepness/slope) of f(x).
# Here, SymPy differentiates x² with respect to x.
# Result: 2*x
dx_f = diff(f)

# Print the derivative formula.
# Output:
# 2*x
#
# Meaning:
# 2*x is NOT the steepness at one point.
# It is a formula that tells the steepness of the graph at ANY value of x.
#
# Examples:
# x = 1  -> steepness = 2
# x = 2  -> steepness = 4
# x = 5  -> steepness = 10
print(dx_f)