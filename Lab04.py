import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_data(filename,index):
    df=pd.read_csv(filename)
    df[index]=pd.to_datetime(df[index])
    df.set_index(index,inplace=True)
    return df

#Set resolution    
def set_resolution(df,period):
   df=df.resample(period).mean()
   print(df)
   print(df.describe())
   return df

df=read_data("fridge_317.csv","timestamp")
df=set_resolution(df,'d')
df2=read_data("air_conditioner_222.csv","timestamp")
df2=set_resolution(df2,'d')

# df=df.resample('d').mean()
# print(df)
# print(df.describe())

# Combine method 1:concetenation
concat_df=pd.concat([df,df2],axis='columns')
# print(concat_df.columns[0],' ',concat_df.columns[1])
print(concat_df)
print(concat_df.describe())

# combline method 2:Merge
# merge_df=df.merge(df2,on='timestamp',how='outer',suffixes=['_fridge','_AC'])
# print(merge_df)
# print(merge_df.describe())

#combline method 3: join
join_df=df.join(df2,how='outer',lsuffix='_fridge',rsuffix='_AC',sort=True)#Join understood that the index will be used ass the axis -xrange
print(join_df)
print(join_df.describe())

#used in assigment 

#set resolution


join_df.plot()
plt.show()