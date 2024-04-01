import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("airquality.csv")

print(df)
print(df.describe()) # Show the basic statistics abou the data.

def rms(df, M):
    Mp2 = M + '^2'
    df2 = df[['MonthName', M]]
    df2.set_index('MonthName', inplace=True)
    df2[Mp2] = df2[M] ** 2 # Create a new column.
    print('Square sum:', df2[Mp2].sum())
    print('Mean square:', df2[Mp2].sum()/df2[Mp2].count())
    rms = np.sqrt(df2[Mp2].sum()/df2[Mp2].count())
    print('Root mean square (RMS):', rms)
    
    del df2[Mp2] # Delete the new column.
    
    return df2,rms

# Plot in the line graph
def figure(df, rms, fig, loc):
    ax1 = plt.subplot2grid((2,2), loc)
    df2.plot(ax=ax1)
    plt.axhline(y=rms, color='r', linestyle='-')
    
#Hadle missing data:method 1: Remove missing data
# df.dropna(how='all',inplace=True)#remove not a number(NAN)fir all attributes. 

# Hadle missing data:method 2: Fill data forward.
# df.fillna(method='ffill', inplace=True) #fill farward,fill with previous value.

#Hadle missing data :method 3:fill data backward
#df.fillna(method='bfill', inplace=True)#fill backward,fill with next record value.

#Hadle missing data :method 4:Custom fill 
df.fillna(value=0,limit=10000,inplace=True)#



fig = plt.figure()
df2,rmsVal = rms(df, M='Ozone')
figure(df2, rmsVal, fig, (0,0))

df2,rmsVal = rms(df, M='Solar.R')
figure(df2, rmsVal, fig, (0,1))

df2,rmsVal = rms(df, M='Wind')
figure(df2, rmsVal, fig, (1,0))

df2,rmsVal = rms(df, M='Temp')
figure(df2, rmsVal, fig, (1,1))

plt.show()