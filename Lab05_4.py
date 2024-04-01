import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df=pd.read_csv('device1.csv')

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

fig=make_subplots(rows=1,cols=2,
                  subplot_titles=("<b>Pie chart</b>","<b>Bar graph</b>"),
                  specs=[[{"type":"domain"},{"type":"xy"}]]
                  )
                  
fig.update_layout(title_text='IoT devices')

fig.add_trace(
    go.Pie(labels=new_df['os_vendor'],
            values=new_df['counts']),
            row=1,col=1
            )

fig.add_trace(
    go.Bar(x=new_df['os_vendor'],
            y=new_df['counts'],
            name='Number of devices'),
            row=1, col=2
            
            )
       
fig.show()