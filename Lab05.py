import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('airquality.csv')
print(df)
print(df.corr())
# print(df[['Solar.R','Ozone']].corr())# 35% correlated
# print(df[['Solar.R','Temp']].corr())# 28% correlated
# print(df[['Solar.R','Wind']].corr())# low -5% correlated
# print(df[['Ozone','Temp']].corr())# high 70% correlated
# print(df[['Ozone','Wind']].corr())# -60% correlated
# print(df[['Temp','Wind']].corr())# -46% correlated

# print(df.pct_change()) 