# Facet Grid in seaborn

import matplotlib.pyplot as plt
import seaborn as sns

df=sns.load_dataset("tips")
print(df.head())

fg=sns.FacetGrid(df,col='day', hue='sex', palette="viridis")

fg.map(plt.scatter, "total_bill", "tip").add_legend()
plt.show()
