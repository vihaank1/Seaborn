# Count plot for exercise dataset and use diet feature for plot

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df=sns.load_dataset("exercise")
print(df.head())

sns.countplot(x="diet", data=df, hue="kind",
              palette="dark:yellow", saturation=0.4)
plt.show()
