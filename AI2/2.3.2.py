import pandas as pd

url = "https://raw.githubusercontent.com/akmand/datasets/main/california_housing.csv"
dataframe = pd.read_csv(url)
print(dataframe.head(3))
print(dataframe.tail(3))
print(dataframe.shape)
print(dataframe.describe())
print(dataframe[3:6])
print(dataframe[dataframe['ocean_proximity'] == "INLAND"].head(5))
