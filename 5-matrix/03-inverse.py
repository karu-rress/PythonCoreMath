import numpy as np

A = np.matrix([[5, 3], [2, 1]])
B = np.linalg.inv(A)

print(B)

print((A * B).astype(np.int64))