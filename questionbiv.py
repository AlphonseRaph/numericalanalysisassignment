#!/usr/bin/env python3
#4. Linear Regression
from sklearn.linear_model import LinearRegression

# Define the data points
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 3, 3, 2, 5])

# Create the model and fit it
model = LinearRegression()
model.fit(X, y)

# Predict
y_pred = model.predict(X)

# Plot the results
plt.scatter(X, y, label='Data')
plt.plot(X, y_pred, label='Linear fit', color='red')
plt.legend(loc='best')
plt.show()

print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")
