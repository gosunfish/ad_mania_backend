import argparse
import ConfigParser
import logging
import os.path

logger = logging.getLogger(__name__)


class Config(object):

    def __init__(self):
        config = dict()
        config_parser = ConfigParser.ConfigParser()
        config_parser.read('../app.ini')
        config['DB_LOGIN'] = config_parser.get('parameters', 'db_login')
        config['DB_PW'] = config_parser.get('parameters', 'db_pw')
        config['DB_HOST'] = config_parser.get('parameters', 'db_host')
        config['DB_NAME'] = config_parser.get('parameters', 'db_name')
        config['CJ_AUTH'] = config_parser.get('parameters', 'cj_auth')
        config['CJ_URL'] = config_parser.get('parameters', 'cj_url')
        config['LOG_FILE'] = config_parser.get('parameters', 'log_file')
        if os.path.isfile('../development_mode'):
            config['LOGGING_LEVEL'] = config_parser.get('development', 'logging_level')
        else:
            config['LOGGING_LEVEL'] = config_parser.get('production', 'logging_level')

        # Override with command line arguments
        parser = argparse.ArgumentParser()
        parser.add_argument("--dblogin", help="Login for mysql database.")
        parser.add_argument("--dbpw", help="Password for mysql database.")
        parser.add_argument("--dbhost", help="Host name for mysql database.")
        parser.add_argument("--dbname", help="Database name for mysql database.")
        parser.add_argument("--cjurl", help="cj affiliate platform api url.")
        parser.add_argument("--cjauth", help="cj affiliate platform authentication code.")
        parser.add_argument("--logging_level", help="Logging Level")
        parser.add_argument("--log_file", help="Log File Name")
        args = parser.parse_args()
        config['DB_LOGIN'] = args.dblogin if args.dblogin else config['DB_LOGIN']
        config['DB_PW'] = args.dbpw if args.dbpw else config['DB_PW']
        config['DB_HOST'] = args.dbhost if args.dbhost else config['DB_HOST']
        config['CJ_AUTH'] = args.cjauth if args.cjauth else config['CJ_AUTH']
        config['CJ_URL'] = args.cjurl if args.cjurl else config['CJ_URL']
        config['LOGGING_LEVEL'] = args.logging_level if args.logging_level else config['LOGGING_LEVEL']
        config['LOG_FILE'] = args.log_file if args.log_file else config['LOG_FILE']

        self.config = config

        logging_level = getattr(logging, config.get('LOGGING_LEVEL', 'INFO'))
        log_file = config.get('LOG_FILE', '/var/log/admania.log')
        logging.basicConfig(level=logging_level, filename=log_file)

    def __getitem__(self, item):
        return getattr(self, item) if item in self.config else KeyError(item)