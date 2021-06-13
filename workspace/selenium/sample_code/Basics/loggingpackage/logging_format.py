import logging


logging.basicConfig(format = "%(asctime)s: %(levelname)s: %(message)s",
                    filename="test.log",
                    level=logging.DEBUG,
                    datefmt='%m/%d/%Y %I:%M:%S %p')

logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")