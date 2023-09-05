import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('data2.CSV')

sns.pairplot(data,hue='Friday')
plt.show()