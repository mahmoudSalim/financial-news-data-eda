import logging
import os

from utils.constants import LOGGING_LEVEL


logging.basicConfig(level=LOGGING_LEVEL)


def create_logger() -> logging.Logger:
    # Create the Logger
    _logger = logging.getLogger("sentiment_logger")
    _logger.setLevel(LOGGING_LEVEL)

    # Create the Handler for logging data to a file
    log_file_path = os.path.join(os.getcwd(), 'sentiment.log')
    logger_handler = logging.FileHandler(log_file_path)
    logger_handler.setLevel(LOGGING_LEVEL)

    # Create a Formatter for formatting the log messages
    logger_formatter = logging.Formatter(
        '[%(asctime)s ] - %(name)s - %(levelname)s - %(message)s')

    # Add the Formatter to the Handler
    logger_handler.setFormatter(logger_formatter)

    # Add the Handler to the Logger
    _logger.addHandler(logger_handler)
    _logger.info('Completed configuring logger()!')

    return _logger
