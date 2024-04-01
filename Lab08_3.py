import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics

def performance(x,y,y_predict):
    print('Accuracy:',classifier.score(x,y))
    cm=metrics.confusion_matrix(y,y_predict)
    print('Confusion matrix for traing : \n',cm)
    print(metrics.classification_report(y,y_predict))
    return cm
#Render heatmap    
def heatmap(df,fig,loc,title):
    ax1=plt.subplot2grid((1,2),loc)
    ax1.set_title(title)
    sns.heatmap(df,ax=ax1,annot=True,cmap='YlGnBu')
    

df=pd.read_csv('Iris.csv')

x=df[['PetalLengthCm','PetalWidthCm']]
y=df['Species']
# print(y)

#split x and y into training and testing sets.

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,random_state=0)

classifier=LogisticRegression()
classifier.fit(x_train,y_train)
y_predict=classifier.predict(x_train)


#prediction
y_train_predict=classifier.predict(x_train)
y_test_predict=classifier.predict(x_test)


# Accuracy,confusion matrix
print("performance for training")
cm_train=performance(x_train,y_train,y_train_predict)
print("performance for testing")
cm_test=performance(x_test,y_test,y_test_predict)

fig=plt.figure()
df_cm_train=pd.DataFrame(cm_train)
df_cm_test=pd.DataFrame(cm_test)
heatmap(df_cm_train,fig,(0,0),'Confusion matix heatmap for training set')
heatmap(df_cm_test,fig,(0,1),'Confusion matix heatmap for testing set')

plt.show()


#performance for training: Accuracy,confusion matrix
#print('Accuracy for training :',classifier.score(x_train,y_train))

# from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
# cm=metrics.confusion_matrix(y_train,y_predict)
# print('Confusion matrix for traing : \n',cm)
# print(classification_report(y_train,y_predict))

# fig,ax=plt.subplots()
# classNames=['Setosa','Versicolor','Virginica']
# tickMarks=np.arange(len(classNames))
# plt.xticks(tickMarks,classNames)
# plt.yticks(tickMarks,classNames)
# sns.heatmap(pd.DataFrame(cm),annot=True,cmap='YlGnBu')
# ax.xaxis.set_label_position('top')
# ax.set_title('Confusion matix heatmap for training set')
# plt.show()

#performance for testing: Accuracy,confusion matrix
# print('Accuracy for training :',classifier.score(x_test,y_test))
# y_predict=classifier.predict(x_test)
# cm=metrics.confusion_matrix(y_test,y_predict)
# print('Confusion matrix for traing : \n',cm)
# print(classification_report(y_test,y_predict))


