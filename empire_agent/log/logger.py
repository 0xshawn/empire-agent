import logging
import os


class Log(object):

    def __init__(self):
        self.LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'
        self.DATE_FORMAT = '%Y-%d-%m %H:%M:%S'
        self.LOG_PATH = '/var/log/empire-agent/'

    def log_init(log_format=LOG_FORMAT,
                 log_path=LOG_PATH, date_format=DATE_FORMAT):
        if not os.path.exists(log_path):
            os.makedirs(log_path)

        logging.basicConfigfilename = log_path + 'empire-agent.log',
        format = log_format,
        datefmt = date_format,
        level = logging.DEBUG
        logger = logging.getLogger()

        return logger
