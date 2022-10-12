import numpy as np

A = np.array([0, 1] * 4 * 8).reshape(8, 8)
for i in range(1, 8, 2):
    A[i] = A[i][::-1]
print(A)
