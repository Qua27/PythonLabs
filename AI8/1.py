import matplotlib.pyplot as plt

import numpy as np
from sklearn.cluster import KMeans

x = np.array([[5, 3], [10, 15], [15, 12], [24, 10], [30, 45], [85, 70], [71, 80], [60, 78], [55, 52], [80, 91]])
plt.scatter(x[:, 0], x[:, 1], s=20)
plt.show()
kmeans = KMeans(n_clusters=5)
kmeans.fit(x)
y_kmeans = kmeans.predict(x)
print(y_kmeans)
