#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2 May 2021

@author: lordmike
'''

import configparser
import logging

from logging import _levelToName
from setup_apps import util

logger = logging.getLogger('config_test')
logger.propagate = False  # Do not propagate the log up to parent
_CONFIGFILE = None

def raiseErrorFileNotFound(file: str):# -> NoReturn:
    # https://docs.python.org/3/library/exceptions.html
    if not util.is_file(file):
        raise FileNotFoundError(str(file))

def getConfigFileContent() -> configparser.RawConfigParser:
    global _CONFIGFILE
    if _CONFIGFILE is not None:
        return _CONFIGFILE

    _CONFIGFILE = configparser.RawConfigParser(allow_no_value=True)
    conffile = 'test.ini'
    logger.error('I will try to use default config file.')
    logger.info('Config path: ' + str(conffile))

    if not util.is_file(conffile):
        # TODO: create test.ini with default values
        temp = configparser.RawConfigParser()
        temp.add_section('section')
        temp.set('section', 'option', 'value')
        #logger.debug("[{}]\n".format('section_name'))
        with open(conffile, 'w') as configfile:
            temp.write(configfile)
            #configfile.write("[{}]\n".format('section_name'))
        pass
    raiseErrorFileNotFound(conffile)

    logger.info('starting to read test.ini (' + str(conffile) + ')...')

    _CONFIGFILE.read(conffile)
    return _CONFIGFILE

def getFromConfigfile(section: str, option: str, default: str=None, reraise: bool=False,
                      must_have_value: bool=True) -> str:
    configfile = getConfigFileContent()
    value = default
    try:
        value = configfile.get(section, option)
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        if reraise:
            logger.error(str(e))
            raise e

        logger.info(str(e))
        return default

    if must_have_value and not value:
        raise ValueError('test.ini [' + str(section) + '] ' + \
                         str(option) + ' <-> Must have value.')

    return value

def str2bool(string: str, default: bool=None) -> bool:
    try:
        return string.lower() in ['true', '1']
    except (ValueError, TypeError, AttributeError):
        return default

def toString(section: str, option: str, result, value: str, level_to_name=False) -> str:
    level = ''
    if level_to_name:
        level = ' [' + str(_levelToName.get(result)) + '] '

    return 'test.ini:  ' + '[' + str(section) + '] ' + str(option) + ': ' + \
        str(result) + level + ' (' + str(value) + ')'

def isTrue(section: str, option: str, default: bool=False) -> bool:
    value = getFromConfigfile(section, option)
    result = str2bool(value, default=default) # what is returned if value == None

    logger.info(toString(section, option, result, value))

    return result


class TestUtil():
    _section = 'test_util.py'

    def __init__(self, params=None):
        '''
        Constructor
        '''


class TestXml():
    _section = 'test_xml.py'
    log_to_file = False
    #log_to_file = isTrue(_section, 'log_to_file', default=False)

    def log_to_file(self):
        self.log_to_file = isTrue(self._section, 'log_to_file', default=False)


class Config(object):
    '''
    classdocs
    '''
    #test_util = TestUtil()
    #test_xml = TestXml()

    def __init__(self):
        '''
        Constructor
        '''
        self.test_util = TestUtil()
        self.test_xml = TestXml()

    @staticmethod
    def read_values_from_file():
        #Config.TestXml.log_to_file = isTrue(_section, 'log_to_file', default=False)
        #Config.TestXml.log_to_file()
        conf = Config()
        conf.test_xml.log_to_file()
        return conf

    @staticmethod
    def write_ini_file():
        pass

