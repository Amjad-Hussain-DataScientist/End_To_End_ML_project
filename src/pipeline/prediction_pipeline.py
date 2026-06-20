# libraries 
import sys
import pandas as pd
from src.exception import CustomeException
from src.utils import load_object

# creatinf first function

class PredictPipeline:
    def __init__(self):
        pass
    # here we will make another function which make prediction
    def predict(self, features):
        try:
            # here we bring pkl file from artifact giving path
            model_path = r'artifacts\model.pkl'
            preprocessor_path = r'artifacts\preprocessor.pkl'
            # now loading the model_path using load_object from utils 
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            # once we load the pkl of prefrocessor then we transform the feature
            data_scaled = preprocessor.transform(features)
            # after transformation model do the prediction
            preds = model.predict(data_scaled)
            return preds 
        except Exception as e:
            raise CustomeException(e,sys)


class CustomData:
    def __init__(self,
                 gender:str,
                 race_ethnicity:str,
                 parental_level_of_education,
                 lunch:str,
                 test_preparation_course:str,
                 math_score:int,
                 reading_score:int):
        # now creating variable using self
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.math_score = math_score
        self.reading_score = reading_score
    #now making function which return all data in the form of datafram
    def get_data_as_data_frame(self):
      try:
        custom_data_input_dict = {
           "gender":[self.gender],
           "race_ethnicity": [self.race_ethnicity],
           "parental_level_of_education":[self.parental_level_of_education],
           "lunch":[self.lunch],
           "test_preparation_course":[self.test_preparation_course],
           "math_score":[self.math_score],
           "reading_score":[self.reading_score]

        }
        # now change custom_data_input_dict intp df
        return pd.DataFrame(custom_data_input_dict)
      except Exception as e:
        raise CustomeException(e,sys)
