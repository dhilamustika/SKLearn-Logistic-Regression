# -*- coding: utf-8 -*-
"""notebook.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rvzdCD67w-V5ZYRD6g5co74Sx22vYguy
"""

from google.colab import files

uploaded = files.upload()

import pandas as pd

df = pd.read_csv('Social_Network_Ads.csv')

df.head()

df.info()

# remove unnecessary column
data = df.drop(columns=['User ID'])

# run a one-hot encoding process
data = pd.get_dummies(data)
data

# divide the dataset into features (X) and labels (y)
predictions = ['Age' , 'EstimatedSalary' , 'Gender_Female' , 'Gender_Male']

X = data[predictions]
y = data['Purchased']

# normalize the dataset
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X)
scaled_data = scaler.transform(X)
scaled_data = pd.DataFrame(scaled_data, columns= X.columns)
scaled_data.head()

# split the dataset into train and test sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(scaled_data, y, test_size=0.2, random_state=1)
print(len(y_test))

# train the model
from sklearn import linear_model

model = linear_model.LogisticRegression()
model.fit(X_train, y_train)

# test the trained model
model.score(X_test, y_test)