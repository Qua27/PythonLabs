import numpy as np
from matplotlib import pyplot as plt

x = np.array([3.0, 3.2, 3.4, 3.6, 3.8, 4.0])
y = np.array([6.0, 2.0, 6.0, 4.0, 3.0, 4.0])
m = np.vstack((x, np.ones(6))).T
s = np.linalg.lstsq(m, y, rcond=None)[0]
x_p = np.linspace(2, 5, 101)
plt.plot(x, y, 'o', label='Source Data', markersize=10)
plt.plot(x_p, s[0] * x_p + s[1], 'r', label='Linear Extrapolation', lw=2)
plt.grid()
plt.legend()
plt.show()
m = np.vstack((x ** 2, x, np.ones(6))).T
s = np.linalg.lstsq(m, y, rcond=None)[0]
plt.plot(x, y, 'o', label='Source Data', markersize=10)
plt.plot(x_p, s[0] * x_p ** 2 + s[1] * x_p + s[2], 'r',
         label='Quadratic Polynomial Extrapolation', lw=2)
plt.grid()
plt.legend()
plt.show()
