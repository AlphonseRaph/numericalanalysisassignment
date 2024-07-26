#!/usr/bin/env python3
#3. Curve Fitting
import scipy.optimize as spo
import matplotlib.pyplot as plt
import numpy as np

# Define the data points
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([0, 0.8, 0.9, 0.1, -0.8, -1.0])

# Define the model function
def model(x, a, b, c):
    return a * np.sin(b * x + c)

# Fit the model to the data
params, params_covariance = spo.curve_fit(model, x_data, y_data, p0=[1, 1, 0])

# Plot the results
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, model(x_data, *params), label='Fitted function', color='red')
plt.legend(loc='best')
plt.show()

print(f"Fitted parameters: {params}")
