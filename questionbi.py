#!/usr/bin/env python3
import sympy as sp

# Define the symbol and the function
x = sp.symbols('x')
f = sp.sin(x) * sp.exp(x)

# Differentiate the function
f_prime = sp.diff(f, x)
print(f"f(x) = {f}")
print(f"f'(x) = {f_prime}")
