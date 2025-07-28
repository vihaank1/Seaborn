# Pair plot

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df=sns.load_dataset("dots")
print(df.head())

sns.pairplot(df,hue="choice", palette='winter')
plt.show()
