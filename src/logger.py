# we ue logging , when ever the execution happen we log that in  file instead to print  information on screen

import logging # main logging system in python, Helps you record messages (info, warnings, errors)
import os # operating system helper module , work with file and path
from datetime import datetime

#creating log_file

LOG_FILE =f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# give path to log file

logs_path  = os.path.join(os.getcwd(),"logs",LOG_FILE)

os.makedirs(logs_path,exist_ok=True) # use to keep appending inside the file

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# for logging setup

logging.basicConfig(

    filename=LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s -%(levelname)s -%(message)s",
    level = logging.INFO
)

''' to check you exception and logging work 
if __name__=="__main__":
    logging.info("logging is working")

'''
