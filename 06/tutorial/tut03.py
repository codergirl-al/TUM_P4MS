import numpy as np

np.random.seed(42)
A = np.random.rand(10, 3, 4)
W = np.random.rand(4, 5)
C = np.matmul(A, W)

print(C)