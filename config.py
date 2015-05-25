import argparse
import logging

logger = logging.getLogger(__name__)


class Config(object):

    def __init__(self):
        # command line arguments
        parser = argparse.ArgumentParser()
        parser.add_argument("--DB_LOGIN", help="Login for mysql database.")
        parser.add_argument("--DB_PW", help="Password for mysql database.")
        parser.add_argument("--DB_HOST", help="Host name for mysql database.")
        parser.add_argument("--DB_NAME", help="Database name for mysql database.")
        parser.add_argument("--CJ_URL", help="cj affiliate platform api url.")
        parser.add_argument("--CJ_AUTH", help="cj affiliate platform authentication code.")
        parser.add_argument("--LOGGING_LEVEL", help="Logging Level")
        parser.add_argument("--LOG_FILE", help="Log File Name")
        # Place arguments into a dict for easy retrieval
        config = vars(parser.parse_args())

        self.config = config
        logging_level = getattr(logging, config.get('LOGGING_LEVEL', 'INFO'))
        log_file = config.get('LOG_FILE', '/var/log/admania.log')
        logging.basicConfig(format='%(levelname)s: %(asctime)s %(message)s', level=logging_level, filename=log_file)
        logger.debug('Logging Level: {} {}'.format(config['LOGGING_LEVEL'], logging_level))

    def __getitem__(self, item):
        return self.config[item] if item in self.config else KeyError(item)

