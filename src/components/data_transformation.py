'''
the main purpose of data transformation is how we improve the data quality,
changing format of observation, scaling
mainly we will do preprocessing here

'''
# importing libraries
import sys
import os 
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer # column transformer is used to create pipline meaning doing onh, then scaling etc
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
# now importing from existing pakages
from src.exception import CustomeException
from src.logger import logging
from src.utils import save_object

# need to get any input and path required for data transformation components
# code defines the file path where your trained data transformation tool (the preprocessor) will be saved as a pickle (.pkl) file.
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    # loads the settings for the data transformation step. It initializes the class by linking the preprocessor file path (artifacts/preprocessor.pkl) 
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        #this function is responsible for datatransformation
        # creating all tranformation processes here in try and except block

        try:
            # we have doen eda where we have find out what are numerical and categorical feature 
            #brings both in lists
            numerical_columns = ['math_score', 'reading_score']

            categorical_columns = ['gender', 'race_ethnicity', 
                                   'parental_level_of_education', 'lunch',
                                    'test_preparation_course']
            # now creating pipline for transformation
            # first for numerical feature 

            num_pipline = Pipeline(
                steps = [

                    ("imputer",SimpleImputer(strategy = "median")), # handling missing values
                    ('scaler',StandardScaler())
                ]
            )

            # categorical pipline
            cat_pipline = Pipeline(
                steps = [
                    ('impute',SimpleImputer(strategy='most_frequent')),
                    ('one_hot_encoder',OneHotEncoder()),
                    ('scaler',StandardScaler(with_mean=False))

                ]
            
            )
            logging.info('numerical scaling and missing is completed')
            logging.info('categorical encoded and missing is completed')

            # now combine both pipline in one using columnTransform
            preprocessor = ColumnTransformer(
                [("num_pipline",num_pipline,numerical_columns),
                 ("cate_pipline",cat_pipline,categorical_columns)
                
                ]
            )

            return preprocessor
        
        except Exception as e:

            raise CustomeException(e,sys)
    # start data transfromation technic
    def initiate_data_transformation(self,train_path,test_path):
        try:
            #readingin data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("read the train and test data")
            logging.info('getting preprocessing object')

            preprocessing_obj = self.get_data_transformer_object()

            #declar the target column
            target_column_name = 'writing_score'

            # defining the input features for training data
            input_feature_train_df = train_df.drop(columns = ['writing_score'])
            target_feature_train_df = train_df[target_column_name]

            # same for test data
            input_feature_test_df = test_df.drop(columns = ['writing_score'])
            target_feature_test_df = test_df[target_column_name]

            logging.info("Apply preprocessing object on train and test data")
            input_feature_train_arr =preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr,
                              np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr,
                             np.array(target_feature_test_df)]
            logging.info('save preprocessing object')

            # save the pickle file 
            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )
            # return 3 variable
            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )


        except Exception as e:
            raise CustomeException(e,sys)
            


