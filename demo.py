from customer_churn_prediction.logger import get_logger
from customer_churn_prediction.exception import CustomerChurnException
import sys

# Initialize the logger
logger = get_logger(__name__)
print(__name__)

# Test the logger
logger.info("Welcome to the customer churn prediction project")
logger.debug("This is a debug message")
logger.error("This is an error message")
logger.warning("This is a warning message")
logger.critical("This is a critical message")


# Test the exception handling
try:
    raise ValueError("This is a test error")
except ValueError as e:
    logger.error("An error occurred: %s", str(e))
    raise CustomerChurnException(e, sys) from e