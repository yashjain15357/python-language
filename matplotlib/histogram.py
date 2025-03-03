import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

ages= np.random.rand(500)*100

pos=[i for i in range(0,100,10)]
label= [f"{i}-{i+10}" for i in pos]

print(label)
sns.histplot(ages,color="g",
             alpha=0.4,
             kde=True,
             bins=10,
             edgecolor='b')
plt.xticks(ticks=pos,labels=label,rotation=45,ha="left")
plt.title('AGES')
plt.xlabel("Age interval")
plt.ylabel("age")
plt.show()