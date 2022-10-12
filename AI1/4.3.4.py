import csv
from datetime import datetime
from matplotlib import pyplot as plt

companies = ["AAPL", "GOOG", "MSFT"]

for company in companies:
    f = open(company + ".csv", 'r')
    reader = csv.reader(f)
    x, y = [], []
    i = 0
    for row in reader:
        x.append(datetime.strptime(row[0], "%Y-%m-%d"))
        y.append((float(row[2]) + float(row[3])) / 2)
        i += 1
    f.close()
    plt.plot(x, y, label=company)
plt.legend()
plt.show()
