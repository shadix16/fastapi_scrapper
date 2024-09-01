import logging
from logging.handlers import RotatingFileHandler
import os

# Ensure the '.log' directory exists
log_dir = ".log"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Define the log file path
log_file_path = os.path.join(log_dir, "app.log")

# Define the logger and its configuration
logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)

# Define a file handler to store the logs
file_handler = RotatingFileHandler(log_file_path, maxBytes=2000, backupCount=5)
file_handler.setLevel(logging.DEBUG)

# Define a console handler to display logs in the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Define the log format
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
