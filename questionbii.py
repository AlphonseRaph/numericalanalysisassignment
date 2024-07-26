#!/usr/bin/env python3
#2. Numerical Integration
import scipy.integrate as spi
import numpy as np

# Define the function
def func(x):
    return np.sin(x) * np.exp(x)

# Perform numerical integration
result, error = spi.quad(func, 0, np.pi)
print(f"Integral of sin(x) * exp(x) from 0 to pi: {result}")
