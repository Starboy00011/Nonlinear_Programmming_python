# Small Nonlinear Programming Problem


import numpy as np
from scipy.optimize import minimize

# Define the objective fuction
def objective_fuction(x):
    return x[0]**2 + x[1]**2 + x[0]*x[1]

def objective_function_unbounded(x):
    return -x[0]**2 - x[1]**2


# Define the constraints
constraints = ({'type' : 'eq', 'fun' : lambda x : x[0] + x[1] - 1}) # Small Nonlinear Programming Problem
constraints1 = ({'type' : 'eq', 'fun' : lambda x : x[0] + x[1] - 3}) # Infeasible Nonlinear Programming Problem

# Initial guess
x0 = np.array([0.4, 0.6])

# Perform the optimization
result = minimize(objective_fuction, x0, constraints=constraints) # Small Nonlinear Programming Problem
result1 = minimize(objective_fuction, x0, constraints=constraints1) # Infeasible Nonlinear Programming Problem

# Small Nonlinear Programming Problem
# print('Optimal value:',result.fun)
# print('Optimal Solution:', result.x)

# Infeasible Nonlinear Programming Problem
# print('Message:',result1.message)
# print('Success:',result1.success)
# print('Optimal value:',result1.fun)
# print('Optimal Solution:', result1.x)

# Unbounded Nonlinear Programming Problem
result2 = minimize(objective_function_unbounded, x0, constraints=constraints)

print('Message:', result2.message)
print('Success:', result2.success)