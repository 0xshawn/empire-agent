import logging, os

LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'
DATE_FORMAT = '%Y-%d-%m %H:%M:%S'
LOG_PATH = '/var/log/empire-agent/'

def log_init(log_format = LOG_FORMAT,
        log_path = LOG_PATH, date_format = DATE_FORMAT):
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    logging.basicConfig(filename = log_path + 'empire-agent.log',
                       format = log_format,
                       datefmt = date_format,
                       level = logging.DEBUG)
    logger = logging.getLogger()
    global log
    log = logger
