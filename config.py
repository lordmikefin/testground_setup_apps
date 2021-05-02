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
    conffile = 'config.ini'
    logger.error('I will try to use default config file.')
    logger.info('Config path: ' + str(conffile))

    raiseErrorFileNotFound(conffile)

    logger.info('starting to read config.ini (' + str(conffile) + ')...')

    _CONFIGFILE.read(conffile)

def getFromConfigfile(section: str, option: str, default: str=None, reraise: bool=False,
                      must_have_value: bool=True) -> str:
    configfile = getConfigFileContent()
    value = default
    try:
        value = configfile.get(section, option)
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        if reraise:
            # print(__name__ + ".getFromConfigfile(): ERROR: " + str(e))
            logger.error(str(e))
            raise e

        # print(__name__ + ".getFromConfigfile(): INFO: " + str(e))
        logger.info(str(e))
        return default

    if must_have_value and not value:
        raise ValueError('Config.ini [' + str(section) + '] ' + \
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

    return 'config.ini:  ' + '[' + str(section) + '] ' + str(option) + ': ' + \
        str(result) + level + ' (' + str(value) + ')'

def isTrue(section: str, option: str, default: bool=False) -> bool:
    value = getFromConfigfile(section, option)
    result = str2bool(value, default=default) # what is returned if value == None

    logger.info(toString(section, option, result, value))

    return result


class Config(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''

    class TestUtil():
        _section = 'test_util.py'

    class TestXml():
        _section = 'test_xml.py'
        log_to_file = False
        #log_to_file = isTrue(_section, 'log_to_file', default=False)
