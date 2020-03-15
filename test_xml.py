'''
Created on 11 Jan 2020

@author: lordmike
'''

import setup_apps
#import app_source_handler
from setup_apps import util
import json
import app_source_handler

SOURCE_PATH = util.fix_path(util.home_path() + '/LM_ToyBox/setup_apps')
SOURCE_FILE = 'app_source.xml'

if __name__ == '__main__':
    print('Init messsage test_xml.py')
    print('setup_apps.revision: ' + str(setup_apps.__revision__))

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
    '''
    setup_apps.config.init()
    setup_apps.config.download()
    setup_apps.config.install()
    setup_apps.config.configure()
    '''
    print('END')