import os
import sys
import dill 
import numpy as np
import pandas as pd

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    
def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)

def evaluate_models(X_train,y_train,x_test,y_test,models,params):
    try:
        report={}
        fitted_models={}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            param = params[list(models.keys())[i]]
            
            # Handle empty parameter dict
            if param:  # If param has values, use GridSearchCV
                gs = GridSearchCV(model,param,cv=3)
                gs.fit(X_train,y_train)
                model = gs.best_estimator_
            else:  # If param is empty, fit model directly
                model.fit(X_train,y_train)

            y_train_pred=model.predict(X_train)
            y_test_pred=model.predict(x_test)

            train_model_score = r2_score(y_train,y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = test_model_score
            fitted_models[list(models.keys())[i]] = model
        return report, fitted_models
    except Exception as e:
        raise CustomException(e,sys)