import logging
from datetime import datetime
import sys
import os
# Set up logging
log_file=f'{datetime.now().strftime("%Y-%m-%d-%H%M%S")}.log'

logs = os.path.join(os.getcwd(),'logs')
os.makedirs(logs,exist_ok=True)
log_file_path = os.path.join('logs',log_file)
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')