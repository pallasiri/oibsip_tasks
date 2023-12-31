# -*- coding: utf-8 -*-
"""IRIS FLOWER CLASSIFICATION-OASIS

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jJJ5pJYXp9FphTCTZUdHD5-5e8TKAMUE

# IMPORTING LIBRARIES
"""

import pandas as pd
from sklearn.model_selection import train_test_split
#Classifications
from sklearn.svm  import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix       # evaluation parameters

"""# READING DATASET"""

idata=pd.read_excel("/content/Iris.xlsx")

idata

"""**CHECKING LABELS**"""

idata['Species'].value_counts()

"""CHANGING LABELS TO NUMERIC

"""

idata['Species'][idata['Species']=='Iris-setosa']='0'
idata['Species'][idata['Species']=='Iris-versicolor']='1'
idata['Species'][idata['Species']=='Iris-virginica']='2'

idata['Species'].value_counts()

"""# CHECKING FEATURES"""

idata.info()

"""# SPLITTING DATA FOR TRAINING AND TESTING"""

x=idata.iloc[:,:5]
x

y=idata.iloc[:,-1]
y

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=3)

"""# KNN CLASSIFIIER"""

model=KNeighborsClassifier(n_neighbors=3)

model.fit(x_train,y_train)

y_predict=model.predict(x_test)

"""# EVALUATION"""

accuracy=accuracy_score(y_predict,y_test)*100
accuracy

confusion_matrix1=confusion_matrix(y_test,y_predict)
confusion_matrix1

classification_report1=classification_report(y_test,y_predict)
classification_report1

"""# OTHER CLASSIFIERS

**SVC CLASSIFIER**
"""

model8=SVC()
model8.fit(x_train,y_train)
y_predict=model8.predict(x_test)
score8=accuracy_score(y_test,y_predict)*100
score8

"""**RANDOM FOREST CLASSIFIER**"""

model9=RandomForestClassifier()
model9.fit(x_train,y_train)
y_predict=model9.predict(x_test)
score9=accuracy_score(y_test,y_predict)*100
score9

"""**KNN ALGORITHM**"""

model10=KNeighborsClassifier(n_neighbors=1)
model10.fit(x_train,y_train)
y_predict=model10.predict(x_test)
score10=accuracy_score(y_test,y_predict)*100
score10

"""**DECISION TREE CLASSIFIER**"""

model11=DecisionTreeClassifier()
model11.fit(x_train,y_train)
y_predict=model11.predict(x_test)
score11=accuracy_score(y_test,y_predict)*100
score11