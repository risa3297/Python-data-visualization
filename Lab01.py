import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("airquality.csv")

print(df)

print('Number of row ',df.shape[0]) #number of row
print('number of columns',df.shape[1]) #number of columns

print(df.columns) #Header title

print(df.columns[-1]) #Frist colums or data label on the right.

print(df.columns[0])# header title columns for the left

#list all 
for col in df.columns:
    print(col,':',df[col].dtype) #print data label and data type
    
# print(df['Solar_R'].dtype)

print(df.head()) # list first five datasets

print(df.head(10))#list first ten datasets

print(df.tail())#list last five datasets

print(df.tail(8)) #list last eight datasets

print(df.describe()) #show basic statetic of datasets

print(df['Solar.R']) #Print dimension of datasets

d = df.rename(columns={'Solar.R':'Solar_R'},inplace=True)# rename columns name
print(df)
print(df['Solar_R'])#Alternarive to print a dimension of the datasets

# new data frame
M='Temp'
Mp2=M+'^2'
df2= df[['MonthName',M]]
df2[Mp2]=df2[M]**2
df2.set_index('MonthName', inplace=True)
print(df2)
print('Square sum ',df2[Mp2].sum())
print('Mean square:',df2[Mp2].sum()/df2[Mp2].count())
print('Root mean square RMS',np.sqrt(df2[Mp2].sum()/df2[Mp2].count()))
rms=np.sqrt(df2[Mp2].sum()/df2[Mp2].count())
print('Root mean square  RMS',rms)

del df2[Mp2]#delete the columns
df2.plot()
plt.axhline(y=rms,color='r',linestyle='-')
plt.show()




