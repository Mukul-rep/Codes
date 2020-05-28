import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel("C:/Users/rcoem/Desktop/samiksha/OTAI/pr31.xlsx",'Sheet1')
var=df.groupby(['Origin']).sum().stack()
temp=var.unstack()
type(temp)
x_list = temp['Cylinders']
label_list = temp.index
plt.axis("equal")
plt.pie(x_list,labels=label_list,autopct="%1.1f%%") 
plt.title("Pastafarianism expenses")
plt.show()
