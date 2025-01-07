# Beale Function
# A function with multiplt local minima, challenging for optimization algorithms
# Problem Statement : Minimize Beale function, another test function with multiple local minima 
# Objective Function : f(x, y) = (1.5 - x + xy)**2 + (2.25 - x + x(y**2))**2 + (2.625 - x + x(y**3))**2
# Constraints : No Constraints

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from mpl_toolkits.mplot3d import Axes3D

# Objective Function
def beale(vars):
    x, y = vars
    return (1.5 - x + x*y)**2 + (2.25 - x + x*(y**2))**2 + (2.625 - x + x*(y**3))**2

# Initial guess
initial_guess = [1, 1]

# Perform the optimization
result = minimize(beale, initial_guess)

# Extract results
x_opt, y_opt = result.x
optimal_value = beale(result.x)

# Print results
print(f"Optimal value of x: {x_opt}")
print(f"Optimal value of y: {y_opt}")
print(f"Minimum value of Beale’s function: {optimal_value}")

# Plotting
x = np.linspace(-4, 4, 100)
y = np.linspace(-4, 4, 100)
X, Y = np.meshgrid(x, y)
Z = beale([X, Y])

# 3D Surface Plot
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='inferno', edgecolor='none')
ax.scatter(x_opt, y_opt, optimal_value, color='red', s=50, label='Optimal Solution')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Objective Function Value')
ax.set_title('3D Surface plot of Beale’s Function')
ax.legend()

plt.show()