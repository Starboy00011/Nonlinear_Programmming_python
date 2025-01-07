# Sphere Function

# A simple quadratic fuction is often used to check optimization performance.
# Problem Statement : Minimize the sphere function, a simple text function for optimization
# Objective Function : f(x, y) = x**2 + y**2
# Constraints : No Constraints

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from mpl_toolkits.mplot3d import Axes3D

# Objective Function
def sphere_function(vars):
    x, y = vars
    return x**2 + y**2

# Initial guess
initial_guess = [1, 1]

# Perform the optimization
result = minimize(sphere_function, initial_guess)

# Extract results
x_opt, y_opt = result.x
optimal_value = sphere_function(result.x)

# Print results
print(f"Optimal value of x: {x_opt}")
print(f"Optimal value of y: {y_opt}")
print(f"Minimum value of Sphere function: {optimal_value}")

# Plotting
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = sphere_function([X, Y])

# 3D Surface Plot
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='inferno', edgecolor='none')
ax.scatter(x_opt, y_opt, optimal_value, color='red', s=50, label='Optimal Solution')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Objective Function Value')
ax.set_title('3D Surface plot of Sphere Function')
ax.legend()

plt.show()