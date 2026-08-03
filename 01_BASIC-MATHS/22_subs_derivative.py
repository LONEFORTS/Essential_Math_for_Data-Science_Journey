
#HelloWorld 8.22PM
#DATE: 31 JULY 2026 FRIDAY

# This program is about getting derivatives 1. THE TOOLKIT: Go into Python's garage and grab the "SymPy" math toolkit.
# We nickname it "sp" so we don't have to type the whole word "sympy" every time.
import sympy as sp


# 2. THE VARIABLE: Tell Python to treat the letter 'x' as a pure mathematical symbol.
# Without this, Python thinks 'x' is just text (a string) and won't let us use it in formulas.
x = sp.Symbol('x')


# 3. THE CALCULUS: Use SymPy's differentiation tool (sp.diff) to find the derivative.
# We hand it the formula (x**2) and tell it to focus on 'x' as the variable.
# SymPy calculates the derivative as "2*x" and stores this new formula inside a box named "dx_f".
dx_f = sp.diff(x**2, x)  


# 4. THE SWAP & DISPLAY: Look inside the "dx_f" box (which holds the formula 2*x).
# Use ".subs(x, 2)" to find the letter 'x' and swap it out for the number 2.
# This changes "2*x" into "2 * 2", computes the math to get 4, and "print" flashes '4' on your screen.
print(dx_f.subs(x, 2))
