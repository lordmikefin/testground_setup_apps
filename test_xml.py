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
import LMToyBoxPython
from datetime import datetime
import traceback

def conf_root_logger():
    # Default log level.
    logging.basicConfig(level=logging.DEBUG)

def create_formatter(log_log_point: bool=True):
    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
    #formatter = logging.Formatter('%(name)-10s - %(levelname)-4s: %(message)s')
    f_str = '[%(name)-10s] %(levelname)-4s: %(message)s'
    if log_log_point:
        f_str += ' [%(pathname)s:%(lineno)d]'
    formatter = logging.Formatter(f_str)
    return formatter

def create_hand_file(log_file_name: str):
    hand = logging.FileHandler(log_file_name)
    hand.setLevel(logging.DEBUG)
    hand.setFormatter(create_formatter(log_log_point=False))
    return hand

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

def conf_setup_apps_logger(log_file_name: str=''):
    #logger_conf = setup_apps.logger
    logger_conf = logging.getLogger('setup_apps')
    logger_conf.addHandler(create_hand_stdout())
    logger_conf.addHandler(create_hand_stderr())
    if log_file_name:
        logger_conf.addHandler(create_hand_file(log_file_name))

def conf_app_source_handler_logger(log_file_name: str=''):
    logger_conf = logging.getLogger('app_source_handler')
    logger_conf.addHandler(create_hand_stdout())
    logger_conf.addHandler(create_hand_stderr())
    if log_file_name:
        logger_conf.addHandler(create_hand_file(log_file_name))

def conf_LMToyBoxPython_handler_logger(log_file_name: str=''):
    logger_conf = logging.getLogger('LMToyBoxPython')
    logger_conf.addHandler(create_hand_stdout())
    logger_conf.addHandler(create_hand_stderr())
    if log_file_name:
        logger_conf.addHandler(create_hand_file(log_file_name))

def create_logger(log_file_name: str=''):
    logger = logging.getLogger('test_xml')
    logger.addHandler(create_hand_stdout())
    logger.addHandler(create_hand_stderr())
    if log_file_name:
        logger.addHandler(create_hand_file(log_file_name))
    logger.propagate = False
    return logger


SOURCE_PATH = util.fix_path(util.home_path() + '/LM_ToyBox/setup_apps')
SOURCE_FILE = 'app_source.xml'

if __name__ == '__main__':
    log_file_name = ''
    if False:
        log_file_name = 'test.log'
    conf_root_logger()
    conf_setup_apps_logger(log_file_name)
    conf_app_source_handler_logger(log_file_name)
    conf_LMToyBoxPython_handler_logger(log_file_name)
    #LMToyBoxPython.logging_test()
    setup_apps.util.stop_urllib3_logger()

    logger = create_logger(log_file_name)
    logger.info('Start time: ' + str(datetime.now()))
    logger.info('Init messsage test_xml.py')
    logger.error('Error logging test')
    logger.debug('Debug logging test')
    logger.info('setup_apps.revision: ' + str(setup_apps.__revision__))

    try:
        # NOTE: testing raised errors logging
        #raise Exception('Test error')

        # NOTE: Just testing the 'app_source_handler'
        #update_app_source.source.parse(source_file)
        #app_source_handler.source.parse(util.fix_path(SOURCE_PATH + '/' + SOURCE_FILE))
        #source_file = util.fix_path(SOURCE_PATH + '/' + SOURCE_FILE)

        if True:
            setup_apps.config.create_sample(overwrite=True)
        setup_apps.config.print_sample()
        #setup_apps.config.parse(source_file)
        #print('APPS: ' + json.dumps(app_source_handler.source.APPS, sort_keys=True, indent=2))
        if False:
            setup_apps.config.parse()
        if False:
            setup_apps.config.init()
        if False:
            setup_apps.config.download()
        if False:
            setup_apps.config.install()
        if False:
            setup_apps.config.configure()
    #except Exception as err:
    #    logger.error(err)
    except:
        logger.error("Unexpected error: " + str(sys.exc_info()[0]))
        # print stck trace
        # https://docs.python.org/3/library/traceback.html
        #traceback.print_exc()
        formatted_lines = traceback.format_exc()
        logger.error(formatted_lines)

    logger.info('Stop time: ' + str(datetime.now()))
    logger.info('END')
