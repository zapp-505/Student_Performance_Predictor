import sys

def error_message_detail(error,error_detail:sys):
    #take in the traceback object tb only from sys.exc_info,tells where the error happened.
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python scipt name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message
    
#inherit built in Exception class & wraps around errors to provide more info.
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        #Makes sure custom exception behaves like a standard Python exception by passing error obj to parent
        super().__init__(error_message)
        #modify the message for effective printing
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message