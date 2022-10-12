from math import exp, cos, log
from matplotlib import pyplot
from numpy import trapz


def f(a):
    return abs(cos(a * exp(cos(a) + log(a + 1))))


x = range(1, 11)
y = [f(i) for i in x]
pyplot.grid()
pyplot.plot(x, y, c='r')
pyplot.fill_between(x, y)
area = trapz(y)
pyplot.show()
print(area)
