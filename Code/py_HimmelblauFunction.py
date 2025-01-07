# Himmelblau Function

# A function with multiple local minima tests optimization algorithm's ability to find global minima 
# Problem Statement : Minimize Himmelblau's function, which has multiple local minima.
# Objective Function : f(x, y) = ((x**2) + y - 11)**2 + (x + (y**2) - 7)**2
# Constraints : No Constraints

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from mpl_toolkits.mplot3d import Axes3D

# Objective Function
def himmelblau(vars):
    x, y = vars
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

# Initial guess
initial_guess = [0, 6]

# Perform the optimization
result = minimize(himmelblau, initial_guess)

# Extract results
x_opt, y_opt = result.x
optimal_value = himmelblau(result.x)

# Print results
print(f"Optimal value of x: {x_opt}")
print(f"Optimal value of y: {y_opt}")
print(f"Minimum value of Himmelblau’s function: {optimal_value}")

# Plotting
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = himmelblau([X, Y])

# 3D Surface Plot
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='inferno', edgecolor='none')
ax.scatter(x_opt, y_opt, optimal_value, color='red', s=50, label='Optimal Solution')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Objective Function Value')
ax.set_title('3D Surface plot of Himmelblau’s Function')
ax.legend()

plt.show()
