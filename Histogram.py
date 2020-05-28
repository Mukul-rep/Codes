import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel("C:/Users/rcoem/Desktop/samiksha/OTAI/pr31.xlsx",'Sheet1')
fig=plt.figure()
ax = fig.add_subplot(1,1,1)
ax.hist(df['Displacement'],bins = 7)
plt.title('Displacement distribution')
plt.xlabel('Displacement')
plt.ylabel('Cars')
plt.show()
