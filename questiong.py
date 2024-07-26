#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as spi

# Define the data points
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([0, 0.8, 0.9, 0.1, -0.8, -1.0])

# Create the spline interpolator
spline = spi.InterpolatedUnivariateSpline(x_data, y_data)

# Define the points where we want to evaluate the spline
x_new = np.linspace(0, 5, 100)
y_new = spline(x_new)

# Plot the results
plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_new, y_new, label='Spline interpolation', color='red')
plt.title('Spline Interpolation Example')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
