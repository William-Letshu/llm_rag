import logging
from logging.handlers import RotatingFileHandler
import os

log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

def setup_logger(name: str, log_file: str='app.log', level: logging =logging.INFO):
    logger = logging.getLogger(name=name)
    logger.setLevel(level)
    console_handler = logging.StreamHandler()
    file_handler = RotatingFileHandler(log_file, maxBytes=10**5, backupCount=3)
    formatter = logging.Formatter(log_format)
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger