import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    # log_file = "logs/app.log"

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # file_handler = RotatingFileHandler(log_file, maxBytes=1024*1024*5, backupCount=5)
    # file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # logger.addHandler(file_handler)
    logger.addHandler(console_handler)
