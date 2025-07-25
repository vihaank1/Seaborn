# Bar Plot

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = sns.load_dataset("penguins")
print(df)

sns.set(style='darkgrid')
sns.barplot(x="island", y="bill_length_mm",data=df, hue="sex", hue_order=["Female", "Male"],
            palette='icefire', err_kws={'color': 'g'},capsize=0.2)
plt.show()

sns.barplot(x="bill_depth_mm", y="bill_length_mm",data=df, orient="h")
plt.show()
