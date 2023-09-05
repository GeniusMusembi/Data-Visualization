import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('data2.CSV')

sns.barplot(x='Wednesday', y='Thursday', data=data)
plt.xlabel('Wednesday')
plt.ylabel('Thursday')
plt.title('Day Comparison')
plt.show() #bar chart

