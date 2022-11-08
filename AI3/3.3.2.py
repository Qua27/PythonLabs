from sklearn.feature_extraction import DictVectorizer

data_dict = [{"blue": 1, "green": 2},
             {"blue": 4, "green": 3},
             {"blue": 2, "brown": 2},
             {"green": 1, "brown": 3}]
dict_vectorizer = DictVectorizer(sparse=False)
features = dict_vectorizer.fit_transform(data_dict)
print(features)
