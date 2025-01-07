import numpy as np
from scipy.optimize import linprog

c = [-1, -2]
A = [[1, 2], [3, 4]]
b = [4, 10]
x0_bound = (0, None)
x1_bound = (0, None)


res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bound, x1_bound], method='highs')

print('Optimal value:',res.fun)
print('Optimal solution:',res.x)