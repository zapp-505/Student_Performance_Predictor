import logging
import os
from datetime import datetime

#naming convention of the file with time of error and of type log 
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)#creates that folder only if it doesn’t already exist

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

#configure logging to write to a file in a specific format
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s [Line %(lineno)d] [%(name)s] [%(levelname)s] %(message)s",
    level=logging.INFO
)
