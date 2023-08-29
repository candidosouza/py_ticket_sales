import logging
from pythonjsonlogger import jsonlogger


def configure_logger(name):
    # logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
    logger = logging.getLogger(__name__)
    logHandler = logging.FileHandler("logs/app.log")
    formatter = jsonlogger.JsonFormatter()
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)
    logger.setLevel(logging.INFO)
    return logger