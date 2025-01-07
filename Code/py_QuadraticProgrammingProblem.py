# Quadratic Programming Problem
# A quadratic function with linear constraints demonstrates how to handle constraints in optimization.
# Problem Statement : Minimize a quadratic function subject to linear constraints
# Objective Function : f(x, y) = x**2 + 2xy + y**2
# Constraints : x + y >= 1  &  x - y >= 0

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize, LinearConstraint
from mpl_toolkits.mplot3d import Axes3D\


# Objective function
def quadratic_function(vars):
    x, y = vars
    return x**2 + 2*x*y + y**2

# Constarints
def constraint1(vars):
    x, y = vars
    return x + y - 1

def constraint2(vars):
    x, y = vars
    return x - y

# define constraints
constraints = [
    {'type': 'ineq', 'fun': constraint1},
    {'type': 'ineq', 'fun': constraint2}
]

# Initial guess
initial_guess = [0, 0]

# Perform the optimization
result = minimize(quadratic_function, initial_guess, constraints=constraints)

# Extract results
x_opt, y_opt = result.x
optimal_value = quadratic_function(result.x)

# Print results
print(f"Optimal value of x: {x_opt}")
print(f"Optimal value of y: {y_opt}")
print(f"Minimum value of Quadratic function: {optimal_value}")

# Plotting
x = np.linspace(-1, 2, 100)
y = np.linspace(-1, 2, 100)
X, Y = np.meshgrid(x, y)
Z = quadratic_function([X, Y])

# 3D Surface Plot
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='inferno', edgecolor='none')
ax.scatter(x_opt, y_opt, optimal_value, color='red', s=50, label='Optimal Solution')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Objective Function Value')
ax.set_title('3D Surface plot of Quadratic Function')
ax.legend()

plt.show()