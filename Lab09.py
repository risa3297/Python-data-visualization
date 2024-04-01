import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

df=pd.read_csv('play_tennis.csv')
# print(df)

label=LabelEncoder()
df['outlook_']=label.fit_transform(df['outlook'])
df['temp_']=label.fit_transform(df['temp'])
df['humidity_']=label.fit_transform(df['humidity'])
df['wind_']=label.fit_transform(df['wind'])
df['play_']=label.fit_transform(df['play'])
# print(df[['outlook_','temp_','humidity_','wind_','play_']])

x=df[['outlook_','temp_','humidity_','wind_']]
y=df[['play_']]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=100)

classifier=DecisionTreeClassifier(criterion='entropy')
classifier.fit(x_train.astype(int),y_train.astype(int))
tree.plot_tree(classifier)
plt.show()

# preformance
from sklearn import metrics
print('Accuracy for training :',classifier.score(x_train,y_train))
y_predict=classifier.predict(x_test)
cm=metrics.confusion_matrix(y_test,y_predict)
print('Confusion matrix:\n',cm)
print(metrics.classification_report(y_test,y_predict))