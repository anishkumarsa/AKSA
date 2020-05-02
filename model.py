from pandas import read_csv
import pandas as pd 
import random
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 

df=read_csv('Salary_Data.csv')
df1=df.values
X=df1[:,0:1] #Independant variable it must be in 2D array
y=df1[:,1]   #dependant variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)    # Creating the training and testing data                                                 
reg = LinearRegression() # Creating Linear regression model
reg.fit(X_train, y_train) 
y_pred = reg.predict(X_test) #To find Predicted test values against input test values
r_sq = reg.score(X, y) # To find R^2 (corelation between actual and predicted value)
pickle.dump(reg, open('model.pkl','wb')) #create a Pickle file for serialization