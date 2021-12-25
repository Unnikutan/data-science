import matplotlib.pyplot as plt
import numpy as np
import csv

file = open("medal.csv")
csv_reader = csv.reader(file)
header = next(csv_reader)
rows = []
for i in csv_reader:
    rows.append(i)
x = np.array(rows)
coun = x[:,0]
medals = x[:,1]
plt.pie(r,labels=coun,autopct="%1.1f%%")
plt.show()
