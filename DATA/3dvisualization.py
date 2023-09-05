import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data=pd.read_csv('data2.CSV')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = data['Monday']  #columns from the data2.CSV
Y = data['Tuesday']  
Z = data['Wednesday']  

ax.scatter(X, Y, Z, c='b', marker='x')  

ax.set_xlabel('Monday') #name of axis label
ax.set_ylabel('Tuesday')
ax.set_zlabel('Wednesday')
ax.set_title('3D Scatter Plot')

plt.show()
