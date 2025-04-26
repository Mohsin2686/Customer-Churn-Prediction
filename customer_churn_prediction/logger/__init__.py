import logging
import os
from datetime import datetime

# Get the root directory (alternative to from_root)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # Gets current script's directory

# Create log directory path
LOG_DIR = 'logs'
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_DIR_PATH = os.path.join(ROOT_DIR, LOG_DIR)
os.makedirs(LOG_DIR_PATH, exist_ok=True)  # Create directory first

# Full log file path
LOG_FILE_PATH = os.path.join(LOG_DIR_PATH, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)

#print(f"Logging to: {LOG_FILE_PATH}")