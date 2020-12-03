import pandas as pd 
import numpy as np 
import datadotworld as dw
import matplotlib.pyplot as plt 
import sklearn as sk 
import csv

from sklearn.neighbors import NearestNeighbors
from sklearn.naive_bayes import GaussianNB   
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV


import hearty



X = hearty.clean_df.drop(columns = [58])
y = hearty.clean_df[58]


class ModelPreparer:
    
    def __init__(self, X, y, model, params,test_size=0.25):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=test_size)
        self.model = model
        self.params = params
        self.test_size = test_size
        self.best_model = self.return_best_model()
         
            
    def return_best_model(self):
        grid_search = GridSearchCV(self.model(), self.params, cv=5, n_jobs=-1,  scoring = 'accuracy')
        grid_search.fit(self.X_train, self.y_train)
        
        best_params = grid_search.best_params_
        best_model = self.model(**best_params)
        best_model.fit(self.X_train, self.y_train)
        return best_model
        
    @property
    def accuracy(self):
        test_predictions= self.best_model.predict(self.X_test)
        return accuracy_score(self.y_test, test_predictions)
    
    
    
