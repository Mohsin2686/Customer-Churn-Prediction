from customer_churn_prediction.logger import get_logger

# Initialize the logger
logger = get_logger(__name__)
print(__name__)

# Test the logger
logger.info("This is a test log message.")
logger.error("This is a test error message.")