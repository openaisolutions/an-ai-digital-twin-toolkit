import logging
import os
from datetime import datetime

class Logger:
    def __init__(self, log_dir="logs", log_level=logging.INFO):
        self.log_dir = log_dir
        self.log_level = log_level
        self._initialize_logger()

    def _initialize_logger(self):
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        log_file = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
        log_path = os.path.join(self.log_dir, log_file)

        logging.basicConfig(
            filename=log_path,
            level=self.log_level,
            format="%(asctime)s [%(levelname)s]: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

    def info(self, message):
        logging.info(message)

    def warning(self, message):
        logging.warning(message)

    def error(self, message):
        logging.error(message)

    def critical(self, message):
        logging.critical(message)

if __name__ == "__main__":
    logger = Logger()

    # Example: Logging messages
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
