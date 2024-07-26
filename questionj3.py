#!/usr/bin/env python3

import numpy as np

# Function for Power Iteration Method
def power_iteration(A, max_iterations):
    n = A.shape[0]  # Assuming A is a square matrix
    x = np.random.rand(n)  # Initial random vector
    for _ in range(max_iterations):
        x = A @ x  # Matrix-vector multiplication
        x = x / np.linalg.norm(x)  # Normalize the vector
    eigenvalue = np.dot(x, A @ x)  # Rayleigh quotient approximation
    return eigenvalue, x

# Function for QR Algorithm
def qr_algorithm(A, max_iterations):
    n = A.shape[0]  # Assuming A is a square matrix
    eigenvalues = np.zeros(n)
    eigenvectors = np.eye(n)
    for _ in range(max_iterations):
        Q, R = np.linalg.qr(A)
        A = R @ Q
        eigenvectors = eigenvectors @ Q
    for i in range(n):
        eigenvalues[i] = A[i, i]  # Diagonal elements are eigenvalues
    return eigenvalues, eigenvectors

# Example usage
if __name__ == "__main__":
    # Define your matrix A
    A = np.array([[2, -1, 0],
                  [-1, 2, -1],
                  [0, -1, 2]])

    # Number of iterations
    max_iterations = 100

    # Power Iteration
    eigenvalue_pi, eigenvector_pi = power_iteration(A, max_iterations)

    # QR Algorithm
    eigenvalues_qr, eigenvectors_qr = qr_algorithm(A, max_iterations)

    # Output results
    print("Power Iteration Method:")
    print("Dominant Eigenvalue:", eigenvalue_pi)
    print("Corresponding Eigenvector:", eigenvector_pi)

    print("\nQR Algorithm:")
    print("Eigenvalues:", eigenvalues_qr)
    print("Eigenvectors:")
    print(eigenvectors_qr)

