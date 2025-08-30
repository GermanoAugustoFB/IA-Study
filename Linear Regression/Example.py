import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dummy data: study hours (x) and scores (y)
X = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50]).reshape(-1, 1)  # study hours
Y = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95])  # scores

# Create a linear regression model
model = LinearRegression()
model.fit(X, Y)

# Predict scores based on study hours
Y_pred = model.predict(X)

# Print the coefficients
print(f"Coefficient (slope): {model.coef_[0]}") 
print(f"Intercept: {model.intercept_}")

# Plotting the results
plt.scatter(X, Y, color="blue", label="Real data")
plt.plot(X, Y_pred, color="red", label="Fitted line")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.legend()
plt.show()