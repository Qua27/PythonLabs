import numpy as np
from matplotlib import pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = sns.load_dataset('iris')
x_train, x_test, y_train, y_test = train_test_split(
    iris.iloc[:, :-1],
    iris.iloc[:, -1],
    test_size=0.15
)
k_list = [1, 5, 10]
for k in k_list:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(x_train, y_train)
    y_predicted = model.predict(x_test)
    plt.figure(figsize=(10, 7))
    sns.scatterplot(x='petal_width', y='petal_length', data=iris, hue='species', s=70)
    plt.xlabel("Petal length, cm")
    plt.ylabel("Petal width, cm")
    plt.suptitle(f'k = {k}')
    plt.legend(loc=2)
    plt.grid()
    for i in range(len(y_test)):
        if np.array(y_test)[i] != y_predicted[i]:
            plt.scatter(x_test.iloc[i, 3], x_test.iloc[i, 2], color='red', s=150)
    plt.show()
    print(f'k = {k} - accuracy: {accuracy_score(y_test, y_predicted) :.3}')
