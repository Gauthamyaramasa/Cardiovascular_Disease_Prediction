# -*- coding: utf-8 -*-
"""Cardiovascular_Disease_Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mMbF-tk6oq9eBLkO93xDG56CtVz0izQf
"""

import pandas as pd
import numpy as np
import os,sys
import xgboost as xgb
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Read CSV data into a DataFrame
df = pd.read_csv("cardio_train.csv", sep=';')

df.shape

df.tail(5)

df.duplicated().sum()

df.isnull().sum()

df.columns

df.skew()

df=df[df.ap_hi<=250]
df=df[df.ap_lo<=150]
df=df[df.weight<=125]
df=df[df.height<=200]

x=df.loc[:,df.columns!='cardio'].values[:,1:]
x1=df.loc[:,df.columns!='cardio']
y=df.loc[:,'cardio'].values
y1=df.loc[:,'cardio']
x1.hist(figsize=(15,10))
plt.show()

#Scale the features to between -1 and 1
scaler=MinMaxScaler((-1,1))
x1=scaler.fit_transform(x)
y1=y

#Split the dataset
xtrain,xtest,ytrain,ytest=train_test_split(x1, y1, test_size=0.24,random_state=42)

# Train the model
from xgboost import XGBClassifier
model=XGBClassifier()
model.fit(xtrain,ytrain)
predict=model.predict(xtest)

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Create the confusion matrix
cm = confusion_matrix(ytest, predict)

# Plot the confusion matrix heatmap
plt.figure(figsize=(6, 4))
fg = sns.heatmap(cm, annot=True, cmap="Reds", fmt='d')  # Use 'd' for integer formatting
figure = fg.get_figure()

# Add labels and title
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title("Output Confusion Matrix")

# Show the plot
plt.show()

print('True Positive Cases : {}'.format(cm[1][1]))
print('True Negative Cases : {}'.format(cm[0][0]))
print('False Positive Cases : {}'.format(cm[0][1]))
print('False Negative Cases : {}'.format(cm[1][0]))

pre = round(8486 / (8486 + 2767),3)
print("The Precision is:", pre)
rec = round(8486 / (8486 + 3794),3)
print("The Recall is:", rec)
f1_score = round(2 * (pre * rec) / (pre + rec),3)
print("The F1 Score is:", f1_score)

print("The Model Accuracy is:",round(accuracy_score(ytest,predict)*100,3),"%")