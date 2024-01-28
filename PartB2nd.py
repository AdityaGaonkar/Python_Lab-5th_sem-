import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


tips=sns.load_dataset("tips")
print(tips)

x_values=tips['day']
y_values=tips['tip']

print(tips.head(10))

# plt.scatter(x_values,y_values)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()
# Scatter Plot (day vs tip)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='day',y='tip',data=tips)
plt.title('Scatter Plot of day vs tip')
plt.xlabel('Day')
plt.ylabel('Tip')
plt.show()


sns.lineplot(x='day',y='tip',data=tips)
plt.title('line Plot of day vs tip')
plt.xlabel('Day')
plt.ylabel('Tip')
plt.show()
#
# plt.bar(x_values,y_values)
# plt.title('bar Plot of day vs tip')
# plt.xlabel('Day')
# plt.ylabel('Tip')
# plt.show()

sns.barplot(x='day',y='tip',data=tips)
plt.title('bar Plot of day vs tip')
plt.xlabel('Day')
plt.ylabel('Tip')
plt.show()


sns.histplot(tips['total_bill'],bins=20)
plt.title('Histogram of Total Bills')
plt.xlabel('Total Bills')
plt.ylabel('frequency')
plt.show()