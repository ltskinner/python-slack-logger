
import slack_logger

import logging
import logging.config


logger_config_file = './logging.conf'
logging.config.fileConfig(fname=logger_config_file)
logger = logging.getLogger()

logger.info('info log: launched-run.py')

logger.warning('warning log')
logger.error('error log')
logger.critical('critical log')


