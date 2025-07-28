# Cat plot in seaborn for titanic dataset

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df=sns.load_dataset("titanic")
print(df.head())

sns.catplot(x="pclass",y="fare",data=df, hue="sex", palette="crest", kind="point")
plt.show()
