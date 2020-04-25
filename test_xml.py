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

def conf_root_logger():
    # Default log level.
    logging.basicConfig(level=logging.DEBUG)

def create_formatter():
    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
    #formatter = logging.Formatter('%(name)-10s - %(levelname)-4s: %(message)s')
    f_str = '[%(name)-10s] %(levelname)-4s: %(message)s'
    # TODO: parameterize: show file/line
    f_str += ' [%(pathname)s:%(lineno)d]'
    formatter = logging.Formatter(f_str)
    return formatter

def create_hand_stdout():
    hand_stdout = logging.StreamHandler(stream=sys.stdout)
    hand_stdout.setLevel(logging.DEBUG)
    hand_stdout.setFormatter(create_formatter())
    return hand_stdout

def create_hand_stderr():
    hand_stderr = logging.StreamHandler(stream=sys.stderr)
    hand_stderr.setLevel(logging.ERROR)
    #hand_stderr.setFormatter(create_formatter())
    f_str = '[%(name)-10s] %(levelname)-4s: %(message)s [%(pathname)s:%(lineno)d]'
    formatter = logging.Formatter(f_str)
    hand_stderr.setFormatter(formatter)
    return hand_stderr

def conf_setup_apps_logger():
    logger_conf = setup_apps.logger
    logger_conf.addHandler(create_hand_stdout())
    logger_conf.addHandler(create_hand_stderr())

def create_logger():
    logger = logging.getLogger('test_xml')
    logger.addHandler(create_hand_stdout())
    logger.addHandler(create_hand_stderr())
    logger.propagate = False
    return logger


SOURCE_PATH = util.fix_path(util.home_path() + '/LM_ToyBox/setup_apps')
SOURCE_FILE = 'app_source.xml'

if __name__ == '__main__':
    conf_root_logger()
    conf_setup_apps_logger()
    setup_apps.util.stop_urllib3_logger()

    logger = create_logger()
    logger.info('Init messsage test_xml.py')
    logger.error('Error logging test')
    logger.debug('Debug logging test')
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
