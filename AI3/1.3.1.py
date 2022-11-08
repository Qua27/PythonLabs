import numpy as np
from matplotlib import pyplot as plt


def print_distance(obj1, obj2):
    print("Euclidean:", np.linalg.norm(obj1 - obj2))
    print("Squared euclidian:", np.linalg.norm(obj1 - obj2) ** 2)
    print("Chebyshev:", np.linalg.norm(obj1 - obj2, ord=np.inf))
    print("Hamming.", np.linalg.norm(obj1 - obj2, ord=1))


x = np.array([0, 0, 0])
y = np.array([3, 3, 3])
z = np.array([1, 2, 3])
w = np.array([2, 3, 0])
print("Distance between x and y:")
print_distance(x, y)
print("\nDistance between w and z:")
print_distance(w, z)
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(x[0], x[1], x[2])
ax.scatter(y[0], y[1], y[2])
ax.scatter(w[0], w[1], w[2])
ax.scatter(z[0], z[1], z[2])
plt.show()
