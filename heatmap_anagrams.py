# Heatmap

import matplotlib .pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

super = np.linspace(1,10,20).reshape(4,5)
print(super)

sns.heatmap(super, vmin=0, vmax=12, cmap="gist_heat", annot=True)
plt.show()

df=sns.load_dataset("anagrams")
sun=df.drop(columns=["attnr"],axis=1).head(10)
sns.heatmap(sun)
plt.show() 



switch = np.linspace(1,10,10).reshape(2,5)

look = np.array([["a0","a1","a2","a3","a4"],
                 ["b0","b1","b2","b3","b4"]])
print(look)

x=sns.heatmap(switch,vmin=0,vmax=10, cmap="PuOr"
            ,annot=look,fmt="s", linewidth=10, linecolor="green",
            xticklabels=False,yticklabels=False)
x.set(xlabel="Summer",ylabel="Sunny")

plt.show()


