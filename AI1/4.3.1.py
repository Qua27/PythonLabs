from matplotlib import pyplot
import numpy as np

a = np.random.uniform(0, 1, 100)
avg = np.average(a)
median = np.median(a)

data = np.arange(0, 100, 1)
fig = pyplot.figure(figsize=(10, 7))
pyplot.grid()
pyplot.scatter(data, a)
pyplot.show()
