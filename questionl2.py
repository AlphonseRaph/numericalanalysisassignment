#!/usr/bin/env python3
def newton_divided_difference(x_points, y_points, x):
    """
    Perform Newton's Divided Difference interpolation.
    
    Parameters:
    x_points (list of float): The x-coordinates of the data points.
    y_points (list of float): The y-coordinates of the data points.
    x (float): The point at which to evaluate the polynomial.
    
    Returns:
    float: The interpolated value at x.
    """
    n = len(x_points)
    divided_diff = [[0 for _ in range(n)] for _ in range(n)]
    
    # Initialize divided difference table
    for i in range(n):
        divided_diff[i][0] = y_points[i]
    
    # Calculate divided differences
    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i][j] = (divided_diff[i + 1][j - 1] - divided_diff[i][j - 1]) / (x_points[i + j] - x_points[i])
    
    # Evaluate interpolating polynomial at x
    result = divided_diff[0][0]
    product_term = 1.0
    for i in range(1, n):
        product_term *= (x - x_points[i - 1])
        result += divided_diff[0][i] * product_term
    
    return result

# Example usage:
x_points = [1, 2, 3, 4]
y_points = [1, 4, 9, 16]
x = 2.5  # Example point to evaluate
print(f"Interpolated value at x={x}: {newton_divided_difference(x_points, y_points, x)}")
