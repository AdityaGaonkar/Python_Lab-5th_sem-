import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

filename = r'C:\Users\karth\Downloads\results.csv'
results_data = pd.read_csv(filename)

results_data = results_data.iloc[:, 1:7]
print(results_data)

passfail = {}

subjects = results_data.columns[1:7]
print(subjects)
for subject in subjects:
    pass_count = sum(results_data[subject] >= 35)
    fail_count = sum(results_data[subject] < 35)
    passfail[subject] = {'Pass': pass_count, 'Fail': fail_count}

print(passfail)

sns.scatterplot(x='Maths', y='Science', data=results_data)
plt.title('Scatter Plot of day vs tip')
plt.xlabel('Day')
plt.ylabel('Tip')
plt.show()

results_data.mean().plot(kind='line')
plt.title('Line Plot of Average vs Subject')
plt.xlabel('subjects')
plt.ylabel('average')
plt.show()

pass_fail_df = pd.DataFrame(passfail).transpose()
pass_fail_df.plot(kind='bar')
plt.title('bar plot of pass fail and subjects')
plt.xlabel('subjects')
plt.ylabel('count')
plt.show()

sns.histplot(results_data['Maths'], bins=10, kde=True)
plt.title('Histplot of Maths')
plt.xlabel('Maths')
plt.ylabel('Frequency')
plt.show()
