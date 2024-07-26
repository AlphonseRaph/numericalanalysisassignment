#!/usr/bin/env python3
# Given data points
x_points = [2.00, 4.25, 5.25, 7.81, 9.20, 10.60]
y_points = [7.2, 7.1, 6.0, 5.0, 3.5, 5.0]

# Target x value
x_target = 4.0

# Function to perform linear interpolation
def linear_interpolation(x0, y0, x1, y1, x):
    return y0 + (x - x0) * (y1 - y0) / (x1 - x0)

# Find the interval [x0, x1] where x_target lies
for i in range(len(x_points) - 1):
    if x_points[i] <= x_target <= x_points[i + 1]:
        x0, y0 = x_points[i], y_points[i]
        x1, y1 = x_points[i + 1], y_points[i + 1]
        break

# Perform linear interpolation
y_target = linear_interpolation(x0, y0, x1, y1, x_target)

print(f"The value of y at x = {x_target} is {y_target:.2f}")
