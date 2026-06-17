'''
we are solving here regression problem statemnet and try everything and get the best among all according to data
'''

# libraries

import os
import sys
from dataclasses import dataclass
from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.exception import CustomeException
from src.logger import logging
from sklearn.metrics import r2_score
from src.utils import save_object, evaluate_models

#-----------------------------------------------------------------------
# start model training part

# here is the config file for model trainer
@dataclass
class ModelTrainerConfig:
    train_model_file_path = os.path.join("artifacts","model.pkl")

# make another class which is responsible for model training
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    # make another function where we write all code for training the model

    def initiate_model_trainer(self,train_array,test_array,):
        # we will give the output of data transformation.
        try:
            logging.info("splitting the data into train and test")
            # here we take what is returning in data_transformation
            X_train,y_train,X_test,y_test = (
                train_array[:,:-1], #store all except last column
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            # now create dictionary of all models that we try to use
            models ={
            "Random Forest": RandomForestRegressor(),
            "Decision Tree": DecisionTreeRegressor(),
            "Gradient Boosting": GradientBoostingRegressor(),
            "Linear Regression": LinearRegression(),
            "XGBRegressor": XGBRegressor(),
            "CatBoosting Regressor": CatBoostRegressor(verbose=False),
            "AdaBoost Regressor": AdaBoostRegressor(),
            "knn": KNeighborsRegressor()
                }
            #hyper perameters tuning 
            params={
                "Decision Tree": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    # 'splitter':['best','random'],
                    # 'max_features':['sqrt','log2'],
                },
                "Random Forest":{
                    # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                 
                    # 'max_features':['sqrt','log2',None],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "knn": {
                    'n_neighbors':[3,5,7],
                    'weights': ['uniform', 'distance'],
                    'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],
                    },
                "Gradient Boosting":{
                    # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    # 'criterion':['squared_error', 'friedman_mse'],
                    # 'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Linear Regression":{},
                "XGBRegressor":{
                    'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "CatBoosting Regressor":{
                    'depth': [6,8,10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "AdaBoost Regressor":{
                    'learning_rate':[.1,.01,0.5,.001],
                    # 'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,32,64,128,256]
                }
                
            }


            # now make and see which model perform well 
            model_report:dict = evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,
                                               y_test=y_test,models = models,param = params)
                # evalute_model is commone function  define in utils.py
            # to get best model score from dict 
            best_model_score = max(sorted(model_report.values()))

            # getting best model name 
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            # now to get best model among all 
            best_model = models[best_model_name]

            # make condition and raise custome exception if best_model_score <0.6
            if best_model_score<0.6:
                raise CustomeException("No best Model is found")
            logging.info("best model is found on both training and testing data")

            # do preprocesing by loading preprocessing.pkl from artifact folder
            # for new data we can load , here but we are using train and test data from transformation here

            save_object(
                # save the model
                file_path=self.model_trainer_config.train_model_file_path,
                obj=best_model # convert into pkl file model.pkl
            )

            # to see the predicted o/p for test data
            predicted = best_model.predict(X_test)
            r2score = r2_score(y_test,predicted)

            return r2score
        
        except Exception as e:

            raise CustomeException(e,sys)
# ***************************
# to test it is work or not go to data_ingestion and import from model_trainer 
'''from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer'''
































