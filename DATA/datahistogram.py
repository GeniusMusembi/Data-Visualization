import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('data2.CSV')

data['Monday'].plot.hist()
plt.show() #histogram