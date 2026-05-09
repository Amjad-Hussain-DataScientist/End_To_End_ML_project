# writing own custome exception code, or you can search or google it "exception handling python"

# importing libraries

import sys #sys is like system helper module.
from src.logger import logging

# making function that return error and error detail which is present in sys

def error_message_detail(error,error_detail:sys):
   _,_,exc_tb= error_detail.exc_info() # exc_info return 3 information, but we intrested in 3rd one, and give detail on which line error is occured etc

   file_name = exc_tb.tb_frame.f_code.co_filename
   error_message = "Error has occured in python script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))

   return error_message

   # making class of custom exception which inherate from Exception

   class CustomeException(Exception):
      def __init__(self,error_message,error_detail:sys):
         super().__init__(error_message) # inherate error message from exception module

         self.error_message = error_message_detail(error_message,error_detail=error_detail)
    
    #print message when error occured
      def __str__(self):
          return self.error_message
      
# so this exception handling and we use it where we require
       