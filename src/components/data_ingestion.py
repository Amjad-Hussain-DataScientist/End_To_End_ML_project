# library for this we need 
import os 
import sys # for custom exception and we import that from src/exception.py
from src.exception import CustomeException # for custom exception and we import that from exception.py
# we also require logging for logging 
from src.logger import logging
#we need to import pandas b/c working with dataframe
import pandas as pd
# after reading we need to split the data into train and test
from sklearn.model_selection import train_test_split

from dataclasses import dataclass 
'''
It is a tool that automatically writes shortcut code for your Python classes. 
It helps you cleanly organize and store your ML project settings
 (like file paths or hyperparameter numbers) without writing repetitive code.
in short it create class variable and avoid to use __init__
'''

#defing class for data_ingestion component

@dataclass # this is a decorator
class DataIngestionConfig:
  train_data_path:str = os.path.join('artifacts','train.csv') # input is train_data_path and their o/p be saved in artifact folder as train.csv
  test_data_path:str = os.path.join('artifacts','test.csv') # input is test_data_path and their o/p be saved in artifact folder as test.
  raw_data_path:str = os.path.join('artifacts','data.csv')

class DataIngestion:
  def __init__(self):
    self.ingestion_config = DataIngestion()

class DataIngestion:
  def __init__(self):
    self.ingestion_config = DataIngestionConfig()
  # make own class that read data from any source 
  def initiate_data_ingestion(self):
    logging.info('Data Ingestion method starts/entered the data ingestion components')
    try:
      df = pd.read_csv('notebook\Data\students.csv') # need this line to be change to getting data from other source
      logging.info('Read the dataset as dataframe')
      # now creating the artifacet w.r.t train_data_path
      os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
      # now for raw data
      df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
      logging.info('Train test split initiated')
      train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
      # to save train set into artifact
      train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
      # to save test set into artifact
      test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
      logging.info('Ingestion of data is completed')
      return(
        self.ingestion_config.train_data_path,
        self.ingestion_config.test_data_path)
    except Exception as e:
      raise CustomeException(e,sys)
    

# run and inititate it we do 
if __name__ == '__main__':
    obj = DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()