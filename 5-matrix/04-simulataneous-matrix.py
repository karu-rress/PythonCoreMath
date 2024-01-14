import numpy as np

A = np.matrix([[5, 3], [2, 1]])
inv_A = np.linalg.inv(A)

B = np.matrix([[9], [4]])
print(inv_A * B) # 연립방정식 해