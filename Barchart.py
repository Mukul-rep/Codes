import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel("C:/Users/rcoem/Desktop/samiksha/OTAI/pr31.xlsx",'Sheet1')
var = df.groupby('Cylinders').Displacement.sum()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('Cylinders')
ax1.set_ylabel('Sum of Displacement')
ax1.set_title("Cylinders wise Sum of Displacement")
var.plot(kind='bar')
plt.show()
