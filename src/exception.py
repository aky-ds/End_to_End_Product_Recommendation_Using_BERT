import os
import sys

class CustomException(Exception):
    def __init__(self, error_message,error_message_detail:sys):
        self.error_message = error_message
        _,_,exc_tb=sys.exc_info()
        self.line_no=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename
    
    def __str__(self):
        return f'Error: {self.error_message}\nIn file: {self.file_name}, line: {self.line_no}'