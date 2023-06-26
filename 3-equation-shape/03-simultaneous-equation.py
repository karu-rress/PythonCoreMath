# 연립방정식 풀이
from sympy import Symbol, solve

a = Symbol('a')
b = Symbol('b')

ex1 = a+b-1
ex2 = 5*a+b-3

print(solve((ex1, ex2)))


# 직교하는 직선
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1, 6)
y = 1/2*x + 1/2
y2 = -2*x + 7

plt.plot(x, y)
plt.plot(x, y2)
plt.axis('equal')
plt.grid(color='0.8')
plt.show()