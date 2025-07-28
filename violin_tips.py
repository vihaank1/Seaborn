# Violin plot for tips dataset, 

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df=sns.load_dataset("tips")
print(df.head())

sns.violinplot(x="day",y="total_bill", data=df, linewidth=2,hue="day",
               palette="gist_earth", inner="stick")
plt.show()
