#!/usr/bin/env python3
def lagrange_interpolation(x_points, y_points, x):
    """
    Perform Lagrange interpolation.
    
    Parameters:
    x_points (list of float): The x-coordinates of the data points.
    y_points (list of float): The y-coordinates of the data points.
    x (float): The point at which to evaluate the polynomial.
    
    Returns:
    float: The interpolated value at x.
    """
    n = len(x_points)
    result = 0.0
    
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    
    return result

# Example usage:
x_points = [1, 2, 3, 4]
y_points = [1, 4, 9, 16]
x = 2.5  # Example point to evaluate
print(f"Interpolated value at x={x}: {lagrange_interpolation(x_points, y_points, x)}")
