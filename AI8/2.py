import matplotlib.pyplot as plt

import seaborn as sns
from sklearn.cluster import KMeans

data = sns.load_dataset('iris')
x = data.iloc[:, :3]
print(x.head(10))
print(x.shape)
plt.scatter(x.iloc[:, 0], x.iloc[:, 1], s=20)
plt.show()
kmeans = KMeans(n_clusters=10)
kmeans.fit(x)
y_kmeans = kmeans.predict(x)
print(y_kmeans)
