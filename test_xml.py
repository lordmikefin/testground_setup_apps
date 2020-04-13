'''
Created on 11 Jan 2020

@author: lordmike
'''

import setup_apps
#import app_source_handler
from setup_apps import util
#import json
#import app_source_handler
import logging
import sys

# Default log level.
logging.basicConfig(level=logging.DEBUG)

#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
#formatter = logging.Formatter('%(name)-10s - %(levelname)-4s: %(message)s')
formatter = logging.Formatter('[%(name)-10s] %(levelname)-4s: %(message)s')
logger_conf = setup_apps.logger
hand_stdout = logging.StreamHandler(stream=sys.stdout)
hand_stdout.setLevel(logging.DEBUG)
hand_stdout.setFormatter(formatter)
hand_stderr = logging.StreamHandler(stream=sys.stderr)
hand_stderr.setLevel(logging.ERROR)
hand_stderr.setFormatter(formatter)
logger_conf.addHandler(hand_stdout)
logger_conf.addHandler(hand_stderr)

logger = logging.getLogger('test_xml')
logger.addHandler(hand_stdout)
logger.addHandler(hand_stderr)
logger.propagate = False

SOURCE_PATH = util.fix_path(util.home_path() + '/LM_ToyBox/setup_apps')
SOURCE_FILE = 'app_source.xml'

if __name__ == '__main__':
    logger.info('Init messsage test_xml.py')
    logger.info('setup_apps.revision: ' + str(setup_apps.__revision__))

    # NOTE: Just testing the 'app_source_handler'
    #update_app_source.source.parse(source_file)
    #app_source_handler.source.parse(util.fix_path(SOURCE_PATH + '/' + SOURCE_FILE))
    #source_file = util.fix_path(SOURCE_PATH + '/' + SOURCE_FILE)

    #setup_apps.config.read_write()
    #setup_apps.config.create_test_xml()
    setup_apps.config.create_sample()
    setup_apps.config.print_sample()
    #setup_apps.config.parse(source_file)
    setup_apps.config.parse()
    #print('APPS: ' + json.dumps(app_source_handler.source.APPS, sort_keys=True, indent=2))
    setup_apps.config.init()
    setup_apps.config.download()
    setup_apps.config.install()
    setup_apps.config.configure()
    logger.info('END')
