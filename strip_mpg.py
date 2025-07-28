# Strip plot for mpg dataset using model_year (feature) and horsepower (target)

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df=sns.load_dataset("mpg")
print(df.head())

sns.stripplot(x="model_year", y="horsepower", data=df[df['model_year'].isin([70,71,72,73])], hue="model_year",
              palette="rocket_r", edgecolor="pink", size=5)
plt.show()
