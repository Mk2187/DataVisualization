print("Hello World")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  #pip install matplotlib
import matplotlib as mpl
#%matplotlib inline
#%matplotlib widget
df =pd.read_csv("data_from_yf.csv")
df.set_index(df['Date'])
fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(df['Date'], df['Close'])  # Plot some data on the axes.
plt.show()