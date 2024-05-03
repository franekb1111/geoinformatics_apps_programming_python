import logging

def setup_logging():
    # Create a custom logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)  # Set to DEBUG to capture all types of logs

    # Create handlers for both file and console
    file_handler = logging.FileHandler('app.log')
    console_handler = logging.StreamHandler()

    # Set level for each handler
    file_handler.setLevel(logging.DEBUG)
    console_handler.setLevel(logging.INFO)

    # Create formatters and add it to handlers
    file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

    file_handler.setFormatter(file_format)
    console_handler.setFormatter(console_format)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger