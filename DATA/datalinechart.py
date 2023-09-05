import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('data2.CSV')

data.plot(x='Tuesday',y='Friday')
plt.show() #line chart