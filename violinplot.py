import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df=pd.read_excel("C:/Users/rcoem/Desktop/samiksha/OTAI/pr31.xlsx",'Sheet1')
sns.violinplot(df['Cylinders'], df['Origin']) 
sns.despine()
plt.show()
