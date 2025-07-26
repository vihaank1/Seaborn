# Scatter plot in seaborn, for mapping relationship between duration and waiting for geysers

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df=sns.load_dataset("geyser")
print(df.head())

sns.scatterplot(x="duration",y="waiting", data=df, hue="kind", style="kind",
                palette="flare")
plt.show()
