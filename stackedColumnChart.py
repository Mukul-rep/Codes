import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel("C:/Users/rcoem/Desktop/samiksha/OTAI/pr31.xlsx",'Sheet1')
var = df.groupby(['Cylinders','Displacement']).Displacement.sum()
var.unstack().plot(kind='bar',stacked=True,  color=['red','blue'], grid=False)
