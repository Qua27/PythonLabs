import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-5, 5, 11)
y = x + np.random.rand(11) - 0.5
x += np.random.rand(11) - 0.5
m = np.vstack([x, np.ones(11)]).T
s = np.linalg.lstsq(m, y, rcond=None)[0]
x_p = np.linspace(-5, 5, 101)
plt.plot(x, y, 'o', label='Source Data', markersize=10)
plt.plot(x_p, s[0] * x_p + s[1], 'r', label='Linear Extrapolation', lw=2)
plt.grid()
plt.legend()
plt.show()

x = np.linspace(-5, 5, 11)
y = x ** 2 + np.random.rand(11) - 0.5
x += np.random.rand(11) - 0.5
m = np.vstack((x ** 2, x, np.ones(11))).T
s = np.linalg.lstsq(m, y, rcond=None)[0]
x_p = np.linspace(-5, 5, 101)
plt.plot(x, y, 'D', label='Source Data')
plt.plot(x_p, s[0] * x_p ** 2 + s[1] * x_p + s[2], '-',
         label='Quadratic Polynomial Extrapolation', lw=2)
plt.grid()
plt.legend()
plt.show()

x = np.linspace(-5, 5, 11)
y = x ** 3 + np.random.rand(11) - 0.5
x += np.random.rand(11) - 0.5
m = np.vstack((x ** 3, x ** 2, x, np.ones(11))).T
s = np.linalg.lstsq(m, y, rcond=None)[0]
x_p = np.linspace(-5, 5, 101)
plt.plot(x, y, 'D', label='Source Data')
plt.plot(x_p, s[0] * x_p ** 3 + s[1] * x_p ** 2 + s[2] * x_p + s[3], '-',
         label='Cubic Polynomial Extrapolation', lw=2)
plt.grid()
plt.legend()
plt.show()
