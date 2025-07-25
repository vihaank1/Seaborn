# Histogram plot for total bill column in tips dataset

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df=sns.load_dataset("tips")
print(df.head())

sns.displot(df["total_bill"], bins=[5,10,15,20,25,30,35,40,45,50],kde=True, rug=True, color="purple")
plt.show()
