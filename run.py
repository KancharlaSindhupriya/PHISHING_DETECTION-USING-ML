from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("phishcoop.csv")
dataset = dataset.drop(labels='id', axis=1)
x = dataset.iloc[: , :-1].values
y = dataset.iloc[: , -1:].values
print(y)


x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.25, random_state =0 )
Classifier = LogisticRegression(random_state=0)
Classifier.fit(x_train, y_train)
y_red = Classifier.predict(x_test)
#predicting the tests set result
y_pred = Classifier.predict(x_test)
#confusion matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
score = Classifier.score(x_test , y_test)
print(score*100,"%")


import Datasetgen as data


def main(url):

    try:
        #checking and predicting
        check = data_set.main(url)
        prediction = Classifier.predict(check)
        if prediction==1:
            return "Warning The website is harmfull for you"
        else:
            return "COOL! You can excess the website" +"\n"+ url

    except:
        return "COOL! You can excess the website" +"\n"+ url





