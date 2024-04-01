import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder #cover string in values
from sklearn.linear_model import LinearRegression 
import plotly.express as px

# List all data labels and data types
def getDataLabels(df):
    for col in df.columns:
        print(col, ': ', df[col].dtype)

df=pd.read_csv('Iris.csv')
# print(df)
# getDataLabels(df)
# print(df.describe())

# Encode string to numeric
numerics=LabelEncoder()
df['SpeciesN']=numerics.fit_transform(df['Species'])
print(df)

x=df[['PetalLengthCm','PetalWidthCm']]
y=df['SpeciesN']

classifier=LinearRegression()
classifier.fit(x,y)#fit into a linear function

#Accuracy
print(classifier.score(x,y))

#Prediction
PL=float(input('Enter petal length : '))
PW=float(input('Enter petal Width : '))
# print("Petal Length:",PL)
# print("Petal Width:",PW)
new_x=[[PL,PW]]
results=int(classifier.predict(new_x))
if results==0:
    print("It is setosa orchid flower.")
elif results==1:
    print("It is versicolor orchid flower.")
elif results==2:
    print("It is virginica orchid flower.")


#print(np.int(classifier.predict([[6.7,2.2]])))

# print('Intercept:\n',classifier.intercept_)
# print('Coefficients:\n',classifier.coef_)

# fig=px.scatter(
    # df,
    # x='PetalLengthCm',#'SepalLengthCm',
    # y='PetalWidthCm',#'SepalWidthCm',
    # color='Species'
    
# )
# fig.show()

