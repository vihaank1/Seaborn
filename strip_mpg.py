# Strip plot for mpg dataset using model_year (feature) and horsepower (target)

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df=sns.load_dataset("mpg")
print(df.head())

sns.stripplot(x="model_year", y="horsepower", data=df)
plt.show()
