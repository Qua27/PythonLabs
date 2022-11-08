import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

url = "https://raw.githubusercontent.com/AnnaShestova/salary-years-simple-linear-regression/master/Salary_Data.csv"
dataframe = pd.read_csv(url)
plt.scatter(dataframe["YearsExperience"], dataframe["Salary"], color='b')
plt.xlabel("Years")
plt.ylabel("Salary, $")
plt.show()
X = dataframe.iloc[:, :-1]
Y = dataframe.iloc[:, 1]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
regressor = LinearRegression()
regressor.fit(X_train, Y_train)
Y_pred = regressor.predict(X_test)
df = pd.DataFrame({"Actual": Y_test, "Predicted": Y_pred})
df.plot(kind='bar')
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()
plt.title('Linear Regression')
plt.scatter(X_test, Y_test, color='gray')
plt.plot(X_test, Y_pred, color='red', linewidth=2)
plt.show()
