import numpy as np

A = np.matrix([[1, 3], [2, 1]])
B = np.matrix([[150, 250], [130, 230]])

print(A * B)


E = np.matrix([[1, 0], [0, 1]]) # 단위행렬

print(A * E)
print(E * A) # 단위행렬은 교환법칙이 성립함.