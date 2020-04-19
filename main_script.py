# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:40:54 2020

@author: DELL
"""
#importing important libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from math import log2
from sklearn.linear_model import LinearRegression 
import pickle


#reading the CSV file 
data = pd.read_csv("Flipkart.csv")

#remove comma's from Price column
def remove_comma(price_string):
    price_string = price_string.split(",")
    return int("".join(price_string))

data["Price"] = data["Price"].apply(remove_comma)

#renaming and replacing phone column with distinct value only
data=data.replace(to_replace=["Mi","MI3"],value="Redmi")
data=data.replace(to_replace=["Moto"],value="Motorola")
data=data.replace(to_replace=["G4"],value="Samsung")

data = pd.get_dummies(data)

data=data.dropna()

#distribution of Target variable
data["Price"].hist()

#converting target variable into normal distribution
data["Price"] = data["Price"].apply(log2)

#train and test split and removing variable RAM from training dataset as it is highly co-related with ROM variable
X_train, X_test, y_train, y_test = train_test_split(data.drop(["Price","RAM"],axis=1),data["Price"], test_size=0.33, random_state=42)

#Scaling numerical columns 
scaler = MinMaxScaler()
X_train=pd.DataFrame(scaler.fit_transform(X_train),columns=X_train.columns,index=X_train.index)
X_test = pd.DataFrame(scaler.transform(X_test),columns=X_test.columns,index=X_test.index)

#Creating as instance of LinearRegression class
model2 = LinearRegression()

#training the model on Training dataset
model2.fit(X_train,y_train)

# Saving model to disk
pickle.dump(model2, open('model1.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model1.pkl','rb'))

final_features = [np.array([4000,32,1,0,0,0])]
prediction = model.predict(final_features)
prediction

print(int(model.predict([[5000,32,0,1,0,0]])))