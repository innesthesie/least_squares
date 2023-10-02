import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def least_squares_function_approximation(x, y, degree):
    # Check if the degree is valid
    if degree < 0:
        raise ValueError("Degree must be a non-negative integer.")

    # Create the Vandermonde matrix
    A = np.vander(x, degree + 1, increasing=True)

    # Compute the least squares solution
    coefficients = np.linalg.lstsq(A, y, rcond=None)[0]

    # Create the fitted polynomial function
    def f(x):
        return np.polyval(coefficients[::-1], x)

    return coefficients, f

# Read data from Excel file
data = pd.read_excel("CVC1.xlsx")  # Replace 'data.xlsx' with your file path

x = data['x'].values
y = data['y'].values

degree = 5

coefficients, f = least_squares_function_approximation(x, y, degree)

print("Coefficients:", coefficients)

polinom = ""
for counter, value in enumerate(coefficients):
    valueWithSign = str(value)

    if value > 0 and counter != degree:
        valueWithSign = "+" + str(value)

    if counter == 0:
        polinom = valueWithSign
    else:
        polinom = valueWithSign + "*x^" + str(counter) + polinom
  
print("Polinom:", polinom)
#print("Fitted function:")
#for xi, yi in zip(x, y):
#    print(f"f({xi}) = {f(xi)}, actual value: {yi}")

# Plot the data points and the fitted function
plt.scatter(x, y, label='Data Points', s=0.1)
x_range = np.linspace(x.min(), x.max(), 100)
plt.plot(x_range, f(x_range), label='Fitted Function', color='red', alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Least Squares Function Approximation')
plt.legend()
plt.grid(True)
plt.show()
