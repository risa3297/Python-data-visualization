import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

df=pd.read_csv('play_tennis.csv')
print(df)

label=LabelEncoder()
df['outlook_']=label.fit_transform(df['outlook'])
df['temp_']=label.fit_transform(df['temp'])
df['humidity_']=label.fit_transform(df['humidity'])
df['wind_']=label.fit_transform(df['wind'])
df['play_']=label.fit_transform(df['play'])
print(df[['outlook_','temp_','humidity_','wind_','play_']])

x=df[['outlook_','temp_','humidity_','wind_']]
y=df[['play_']]

x=np.array(x) # convert from data frame to array

classifier=GaussianNB()
classifier.fit(x,y)


# preformance
from sklearn import metrics
print('Accuracy for training :',classifier.score(x,y))


#new data
new_data=[[2,2,1,1]]#sunny, mild, normal, weak
new_data=[[1,1,0,1]]#rain, hot ,high,strong

y_predict=classifier.predict(new_data)
# print(y_predict)
if y_predict[0]==1:
    print('play tennis')
elif y_predict[0]==0:
    print('no play tennis')