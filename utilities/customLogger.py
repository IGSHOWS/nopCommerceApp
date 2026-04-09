# import logging

# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename=".\\Logs\\automation.log",
#                             format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger

import logging
import os

class LogGen:

    @staticmethod
    def loggen():

        log_dir = os.path.join(os.getcwd(), "Logs")

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_file = os.path.join(log_dir, "automation.log")

        logger = logging.getLogger("nopCommerce")
        logger.setLevel(logging.INFO)

        # prevent duplicate handlers
        if not logger.handlers:

            file_handler = logging.FileHandler(log_file)
            formatter = logging.Formatter(
                '%(asctime)s : %(levelname)s : %(message)s',
                datefmt='%m/%d/%Y %I:%M:%S %p'
            )

            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger