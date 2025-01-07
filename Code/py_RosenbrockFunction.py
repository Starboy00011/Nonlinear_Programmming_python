# Rosenbrock Function

# A function with a narrow, curved valley , is used to test optimization algorithm
# Problem Statement: Minimize the Rosenbrock function, a common test problem for optimization algo
# Objective Function : f(x, y) = ((a - x)**2) + b((y - (x**2))**2) 
# Constraints : No  Constraints

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from mpl_toolkits.mplot3d import Axes3D

# Objective Function
def rosenbrock(vars):
    x, y = vars
    a, b = 1, 100
    return (a-x)**2 + b * (y - x**2)**2

# Intial guess
initial_guess = [0, 0]

# Perform the optimization
result = minimize(rosenbrock, initial_guess)

# Extract results
x_opt, y_opt = result.x
optimal_value = rosenbrock(result.x)

# Print results
print(f"Optimal value of x: {x_opt}")
print(f"Optimal value of y: {y_opt}")
print(f"Minimum value fo Rosenbrock function: {optimal_value}")

# Plotting 
x = np.linspace(-2, 2, 100)
y = np.linspace(-1, 3, 100)
X, Y = np.meshgrid(x, y)
Z = rosenbrock([X, Y])

# 3D Surface Plot 
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='inferno', edgecolor='none')
ax.scatter(x_opt, y_opt, optimal_value, color='red', s=50, label='Optimal Solution')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Objective Function Value')
ax.set_title('3D Surface plot of Rosenbrock Function')
ax.legend()

plt.show()