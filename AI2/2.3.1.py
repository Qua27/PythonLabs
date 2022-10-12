import pandas as pd
from numpy import sqrt

A = pd.Series([1, 1])
B = pd.Series([2, 2])
print(sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2))
