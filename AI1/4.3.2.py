from math import sqrt, exp, sin, cos, log
from matplotlib import pyplot


def f(a):
    y = (sqrt(1 + exp(sqrt(a)) + cos(a ** 2))) / (abs(1 - (sin(a)) ** 3)) + log(abs(2 * a))
    return y


x = range(1, 11)
f = [f(i) for i in x]
g = f[:len(f) // 2]
pyplot.grid()
pyplot.plot(x, f)
pyplot.scatter(x[:len(f) // 2], g)
pyplot.show()

pyplot.scatter(x[:len(f) // 2], g)
pyplot.show()
