import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv('Iris.csv')
print(df)


# label=LabelEncoder()
# df['outlook_']=label.fit_transform(df['outlook'])
# df['temp_']=label.fit_transform(df['temp'])
# df['humidity_']=label.fit_transform(df['humidity'])
# df['wind_']=label.fit_transform(df['wind'])
# df['play_']=label.fit_transform(df['play'])
# print(df[['outlook_','temp_','humidity_','wind_','play_']])

x=df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
y=df[['Species']]

classifier=RandomForestClassifier(n_estimators=100) #default=100 trees
classifier.fit(x,y)

# preformance
from sklearn import metrics
print('Accuracy for training :',classifier.score(x,y))


# new data
# new_data=[[4.7,3.3,1.7,0.18]] #Setosa
# new_data=[[6.6,3.0,4.6,1.4]] #Versicolor
new_data=[[7.0,3.2,5.2,2.4]] #Virginica

# new_data=[[1,1,0,1]]#rain, hot ,high,strong

y_predict=classifier.predict(new_data)
print('probably species is ',y_predict[0])
# if y_predict[0]==1:
    # print('play tennis')
# elif y_predict[0]==0:
    # print('no play tennis')
# print('Accuracy score for traning : ', metrics.accuracy_score(x,y))