import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('APIMS-final.csv')
df['Time']=pd.to_datetime(df['Time'])
df.set_index('Time',inplace=True)

df = df.resample('d').mean() 
# print(df)
# print(df.describe())
pc_df=df.pct_change()
print(pc_df) 

# pc0_df= df
# for city in pc0_df:
    # if(pc0_df[city][0]==1 or pc0_df[city][0]=='NAN'or pc0_df[city][0]==''):
        # pc0_df[city][0]==1
    # pc0_df=(pc0_df[city]-pc0_df[city][0])/pc0_df[city][0]*100.0

fig=plt.figure()
ax1=plt.subplot2grid((1,3),(0,0))
df[['Balik Pulau','Langkawi','Klang','Miri']].plot(ax=ax1)

ax1=plt.subplot2grid((1,3),(0,1))
pc_df[['Balik Pulau','Langkawi','Klang','Miri']].plot(ax=ax1)

# ax1=plt.subplot2grid((1,3),(0,1))
# pc0_df[['Balik Pulau','Langkawi','Klang','Miri']].plot(ax=ax1)


plt.show()