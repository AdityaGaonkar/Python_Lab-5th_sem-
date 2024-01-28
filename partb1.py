import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

print(sns.get_dataset_names())
iris = sns.load_dataset("iris")
x_values = iris['sepal_length'].values.reshape(-1,1)
y_values = iris['sepal_width']
print(iris)
plt.scatter(x_values, y_values)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter plot')
plt.show()

x_mean = np.mean(x_values)
y_mean = y_values.mean()
print(f"mean of x is {x_mean} and y is {y_mean}")

x_median = np.median(x_values)
y_meadian = np.median(y_values)
print(f"median of x is {x_median} and y is {y_meadian}")

x_sd = x_values.std()
y_sd = np.std(y_values)
print(f"sd of x is {x_sd} and y is {y_sd}")

x_var=np.var(x_values)

regression = LinearRegression()
regression.fit(x_values, y_values)
slope = regression.coef_[0]
intercept = regression.intercept_
print(f"{slope} ")

plt.scatter(x_values, y_values)
plt.plot(x_values, regression.predict(x_values), color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
