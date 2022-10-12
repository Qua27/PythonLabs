import numpy as np

size = int(input())
A = np.array([[1] + [0] * (size - 2) + [1]] * size)
print(A)
