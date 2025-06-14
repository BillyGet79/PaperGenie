import logging

logger = logging.getLogger()

format_str = "%(asctime)s %(process)d %(thread)d %(threadName)s %(filename)s:%(lineno)d %(levelname)s %(message)s"
formatter = logging.Formatter(format_str)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)
logger.info("Logging started")
