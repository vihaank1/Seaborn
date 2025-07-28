# Box plot in seaborn tips dataset using day and total_bill features

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df=sns.load_dataset("tips")
print(df.head())

sns.set(style='whitegrid')

sns.boxplot(x="total_bill", y="day", data=df, hue="sex", palette="mako",showmeans=True,
            linewidth=3)
plt.show()
