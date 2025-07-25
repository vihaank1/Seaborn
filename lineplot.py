# Line plot  create a lineplot for relationship between bill length and bill depth for both males and females

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

best = sns.load_dataset("penguins")

print(best.head())


sns.lineplot(x="bill_length_mm", y="bill_depth_mm", data=best,
             hue="sex", style="sex", palette="Accent", markers=["o", ">"], dashes=False)

plt.grid()
plt.title("Penguins")
plt.show()
