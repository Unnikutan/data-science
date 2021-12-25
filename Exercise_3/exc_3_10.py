import matplotlib.pyplot as plt
import numpy as np
x= [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
math=[88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science= [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
plt.scatter(x,math,label="Maths",color="red")
plt.scatter(x,science,color="green",label="science")
plt.xlabel("marks_range")
plt.ylabel("Mark Scored")
plt.title("Scatter Plot")
plt.legend()
plt.show()
