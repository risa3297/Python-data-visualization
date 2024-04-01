import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier

df=pd.read_csv('Iris.csv')
numerics=LabelEncoder()
df['SpeciesN']=numerics.fit_transform(df['Species'])


x=df[['PetalLengthCm','PetalWidthCm']]
y=np.array(df['SpeciesN'])
y=y.reshape(150,1)
# print(y)

classifier=MLPClassifier(activation='logistic',solver='adam',hidden_layer_sizes=[150,3],random_state=0,max_iter=500)
classifier.fit(x,y)

# accuracy
print('Accuracy for traning :',classifier.score(x,y))

