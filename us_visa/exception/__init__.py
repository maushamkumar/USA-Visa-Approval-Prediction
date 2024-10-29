import os 
import sys 

def error_message_detail(error, error_detail:sys): # using sys module this function will figure out in which file which line error occurred
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(file_name.co_filename, exc_tb.tb_lineno, str(error))
    # Once I have to check what is difference between file_name.co_filename and file_name
    return error_message

class USvisaException(Exception):
    def __init__(self, error_message, error_detail):
        def __init__(self, error_message, error_detail):
            """
            :Param error_message: error message in string format
            """
            super().__init__(error_message)
            self.error_message = error_message_detail(error_message, error_detail=error_detail)
            
        def __str__(self):
            return self.error_message