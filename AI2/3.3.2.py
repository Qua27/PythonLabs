import pandas as pd
from sklearn import preprocessing

url = "https://raw.githubusercontent.com/akmand/datasets/master/iris.csv"
dataframe = pd.read_csv(url)
print("Dataframe:")
print(dataframe)
print('\n', "----------------", '\n')
min_max_scale = preprocessing.MinMaxScaler()
z_scale = preprocessing.StandardScaler()
dataframe[["sepal_length_cm"]] = min_max_scale.fit_transform(dataframe[["sepal_length_cm"]])
print(dataframe)
dataframe[["sepal_width_cm"]] = z_scale.fit_transform(dataframe[["sepal_length_cm"]])
print(dataframe)
