import logging
import os
from datetime import datetime

# Create a custom logger
def get_logger(logger_name, log_dir="logs", log_file="app.log", level=logging.INFO):
    """
    Creates and returns a custom logger.

    Args:
        logger_name (str): Name of the logger.
        log_dir (str): Directory where log files will be stored.
        log_file (str): Name of the log file.
        level (int): Logging level.

    Returns:
        logging.Logger: Configured logger instance.
    """
    # Ensure the log directory exists
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create a logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # Create a file handler
    log_path = os.path.join(log_dir, log_file)
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(level)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # Create a formatter and set it for both handlers
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Example usage
if __name__ == "__main__":
    logger = get_logger("customer_churn_logger")
    logger.info("Logger initialized successfully.")
    logger.error("This is an error message.")