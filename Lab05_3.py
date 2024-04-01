import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


df=pd.read_csv('device1.csv')

def getDataLables(df):
    for col in df.columns:
      print(col,':',df[col].dtype)
      
# getDataLables(df)
# print(df.describe())

#List 1
ls=['Apple', 'Google','Samsung','LG','Proprietary OS','Motorola','Symbian']
#List 2
counts=[]
for item in ls:
    counts.append(df['os_vendor'].value_counts()[item])
#Genarate a data frame
new_df=pd.DataFrame({
    'os_vendor':ls,
    'counts': counts
})

# print(new_df)
# print(new_df.describe())

fig=px.pie(new_df,
    names='os_vendor',
    values='counts',
    title='IOT devices pie chart')
fig.show()

fig2=px.histogram(new_df,
    x='os_vendor',
    y='counts',
    title='IoT devices pie chart')
fig2.show()