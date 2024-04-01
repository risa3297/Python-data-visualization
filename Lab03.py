import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# List all data labels and data types
def getDataLabels(df):
    for col in df.columns:
        print(col, ': ', df[col].dtype)

def rollingStatistics(df, area, times):
    df['MSUM'] = df[area].rolling(times).sum() # Moving sum.
    df['MA'] = df[area].rolling(times).mean() # Moving average.
    df['MM'] = df[area].rolling(times).median() # Moving median.
    df['MSTD'] = df[area].rolling(times).std() # Moving standard deviation.
    print(df[['MSUM', 'MA', 'MM', 'MSTD']])
    return df[['MSUM', 'MA', 'MM', 'MSTD']]
    
# Plot in the line graph
def figure(df, fig, size, loc, title):
    ax1 = plt.subplot2grid(size, loc)
    df.plot(ax=ax1, title=title)

df = pd.read_csv("APIMS-final.csv")
df['Time'] = pd.to_datetime(df['Time'])
df.set_index('Time',inplace=True)
df.sort_index()
# getDataLabels(df)
print(df.describe())

# Set resolution
df = df.resample('d').mean() # by day, d; by month, M; by year, A.
# print(df)
# print(df.describe())

fig = plt.figure()
# Rolling statistics
areas = ['Balik Pulau', 'Klang', 'Miri', 'Kota Kinabalu']
rows=2
cols=2
i=0

for y in range(0,rows):
    for x in range(0,cols):
        df2 = rollingStatistics(df, areas[i], times=5)
        title = str('API for ') + areas[i]
        figure(df2, fig,(rows,cols),(x,y), title)
        i=i+1

plt.show()