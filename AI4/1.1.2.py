import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def f1(x, b0, b1):
    return b0 + b1 * x


def f2(x, b0, b1, b2):
    return b0 + b1 * x + b2 * x ** 2


def f3(x, b0, b1):
    return b0 + b1 * np.log(x)


def f4(x, b0, b1):
    return b0 * x ** b1


def f0(x, b0, b1, b2):
    return b0 + b1 * np.exp(-b2 * x ** 2)


beta = (0.25, 0.75, 0.5)
x_data = np.linspace(0, 5, 50)
y = f0(x_data, *beta)
y_data = y + 0.05 * np.random.rand(len(x_data))
beta_opt, beta_cov = curve_fit(f0, x_data, y_data)
lin_dev = sum(beta_cov[0])
print(lin_dev)
residuals = y_data - f0(x_data, *beta_opt)
quad_dev = sum(residuals ** 2)
print(quad_dev, '\n')
fig, ax = plt.subplots()
ax.scatter(x_data, y_data)
ax.plot(x_data, y, 'r', lw=2)
ax.plot(x_data, f0(x_data, *beta_opt), 'b', lw=2)
ax.set_xlim(0, 5)
ax.set_xlabel(r"$x$", fontsize=18)
ax.set_ylabel(r"$f(x, \beta)$", fontsize=18)
plt.show()

beta = (0.25, 0.75)
x_data = np.linspace(0, 5, 50)
y = f1(x_data, *beta)
y_data = y + 0.05 * np.random.rand(len(x_data))
beta_opt, beta_cov = curve_fit(f1, x_data, y_data)
lin_dev = sum(beta_cov[0])
print(lin_dev)
residuals = y_data - f1(x_data, *beta_opt)
quad_dev = sum(residuals ** 2)
print(quad_dev, '\n')
fig, ax = plt.subplots()
ax.scatter(x_data, y_data)
ax.plot(x_data, y, 'r', lw=2)
ax.plot(x_data, f1(x_data, *beta_opt), 'b', lw=2)
ax.set_xlim(0, 5)
ax.set_xlabel(r"$x$", fontsize=18)
ax.set_ylabel(r"$f(x, \beta)$", fontsize=18)
plt.show()

beta = (0.25, 0.75, 0.5)
x_data = np.linspace(0, 5, 50)
y = f2(x_data, *beta)
y_data = y + 0.05 * np.random.rand(len(x_data))
beta_opt, beta_cov = curve_fit(f2, x_data, y_data)
lin_dev = sum(beta_cov[0])
print(lin_dev)
residuals = y_data - f2(x_data, *beta_opt)
quad_dev = sum(residuals ** 2)
print(quad_dev, '\n')
fig, ax = plt.subplots()
ax.scatter(x_data, y_data)
ax.plot(x_data, y, 'r', lw=2)
ax.plot(x_data, f2(x_data, *beta_opt), 'b', lw=2)
ax.set_xlim(0, 5)
ax.set_xlabel(r"$x$", fontsize=18)
ax.set_ylabel(r"$f(x, \beta)$", fontsize=18)
plt.show()

beta = (0.25, 0.75)
x_data = np.linspace(0.01, 5, 50)
y = f3(x_data, *beta)
y_data = y + 0.05 * np.random.rand(len(x_data))
beta_opt, beta_cov = curve_fit(f3, x_data, y_data)
lin_dev = sum(beta_cov[0])
print(lin_dev)
residuals = y_data - f3(x_data, *beta_opt)
quad_dev = sum(residuals ** 2)
print(quad_dev, '\n')
fig, ax = plt.subplots()
ax.scatter(x_data, y_data)
ax.plot(x_data, y, 'r', lw=2)
ax.plot(x_data, f3(x_data, *beta_opt), 'b', lw=2)
ax.set_xlim(0, 5)
ax.set_xlabel(r"$x$", fontsize=18)
ax.set_ylabel(r"$f(x, \beta)$", fontsize=18)
plt.show()

beta = (0.25, 0.75)
x_data = np.linspace(0, 5, 50)
y = f4(x_data, *beta)
y_data = y + 0.05 * np.random.rand(len(x_data))
beta_opt, beta_cov = curve_fit(f4, x_data, y_data)
lin_dev = sum(beta_cov[0])
print(lin_dev)
residuals = y_data - f4(x_data, *beta_opt)
quad_dev = sum(residuals ** 2)
print(quad_dev, '\n')
fig, ax = plt.subplots()
ax.scatter(x_data, y_data)
ax.plot(x_data, y, 'r', lw=2)
ax.plot(x_data, f4(x_data, *beta_opt), 'b', lw=2)
ax.set_xlim(0, 5)
ax.set_xlabel(r"$x$", fontsize=18)
ax.set_ylabel(r"$f(x, \beta)$", fontsize=18)
plt.show()
