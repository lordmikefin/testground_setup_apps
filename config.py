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
    logger.info('Config path: ' + str(conffile))

    if not util.is_file(conffile):
        Config.write_ini_file(conffile)

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

    result_str = str(result)
    value_str = ' (' + str(value) + ')'

    temp = 'test.ini:  ' + '[' + str(section) + '] ' + str(option) + ': '
    temp = temp + result_str + level
    temp = temp + value_str
    return temp

def isTrue(section: str, option: str, default: bool=False) -> bool:
    value = getFromConfigfile(section, option)
    result = str2bool(value, default=default) # what is returned if value == None

    logger.info(toString(section, option, result, value))

    return result

def getStr(section: str, option: str, default: str='') -> str:
    value = getFromConfigfile(section, option)
    if value is None:
        result = default
    else:
        result = str(value).strip()

    logger.info(toString(section, option, result, value))

    return result


class TestUtil():
    _section = 'test_util.py'
    _log_to_file = False
    _log_file_name = 'spam_test_util.log'
    _init_testing = False
    _run_command_testing = False
    _logging_testing = False
    _win_only_test = False
    _linux_sudo_test = False

    def __init__(self):
        '''
        Constructor
        '''
        self._log_to_file = None
        self._log_file_name = None
        self._init_testing = None
        self._run_command_testing = None
        self._logging_testing = None
        self._win_only_test = None
        self._linux_sudo_test = None

    def log_to_file(self):
        if self._log_to_file is None:
            self._log_to_file = isTrue(self._section, 'log_to_file', default=False)
        return self._log_to_file

    def log_file_name(self):
        if self._log_file_name is None:
            self._log_file_name = getStr(self._section, 'log_file_name', default=TestUtil._log_file_name)
        return self._log_file_name

    def init_testing(self):
        if self._init_testing is None:
            self._init_testing = isTrue(self._section, 'init_testing', default=False)
        return self._init_testing

    def run_command_testing(self):
        if self._run_command_testing is None:
            self._run_command_testing = isTrue(self._section, 'run_command_testing', default=False)
        return self._run_command_testing

    def logging_testing(self):
        if self._logging_testing is None:
            self._logging_testing = isTrue(self._section, 'logging_testing', default=False)
        return self._logging_testing

    def win_only_test(self):
        if self._win_only_test is None:
            self._win_only_test = isTrue(self._section, 'win_only_test', default=False)
        return self._win_only_test

    def linux_sudo_test(self):
        if self._linux_sudo_test is None:
            self._linux_sudo_test = isTrue(self._section, 'linux_sudo_test', default=False)
        return self._linux_sudo_test


class TestXml():
    _section = 'test_xml.py'
    _log_to_file = False
    #log_to_file = isTrue(_section, 'log_to_file', default=False)
    _log_file_name = 'test_xml.log'
    _create_sample = False
    _overwrite_sample = False
    _parse = False
    _init = False
    _download = False
    _install = False
    _configure = False

    def __init__(self):
        '''
        Constructor
        '''
        self._log_to_file = None
        self._create_sample = None
        self._overwrite_sample = None
        self._parse = None
        self._init = None
        self._download = None
        self._install = None
        self._configure = None

    def log_to_file(self):
        if self._log_to_file is None:
            self._log_to_file = isTrue(self._section, 'log_to_file', default=False)
        return self._log_to_file

    def log_file_name(self):
        if self._log_file_name is None:
            self._log_file_name = getStr(self._section, 'log_file_name', default=TestXml._log_file_name)
        return self._log_file_name

    def create_sample(self):
        if self._create_sample is None:
            self._create_sample = isTrue(self._section, 'create_sample', default=False)
        return self._create_sample

    def overwrite_sample(self):
        if self._overwrite_sample is None:
            self._overwrite_sample = isTrue(self._section, 'overwrite_sample', default=False)
        return self._overwrite_sample

    def parse(self):
        if self._parse is None:
            self._parse = isTrue(self._section, 'parse', default=False)
        return self._parse

    def init(self):
        if self._init is None:
            self._init = isTrue(self._section, 'init', default=False)
        return self._init

    def download(self):
        if self._download is None:
            self._download = isTrue(self._section, 'download', default=False)
        return self._download

    def install(self):
        if self._install is None:
            self._install = isTrue(self._section, 'install', default=False)
        return self._install

    def configure(self):
        if self._configure is None:
            self._configure = isTrue(self._section, 'configure', default=False)
        return self._configure


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
        #conf.test_xml.log_to_file()
        return conf

    @staticmethod
    def write_ini_file(conffile):
        logger.info('I will try to create default config file.')
        # TODO: create test.ini with default values
        temp = configparser.RawConfigParser()
        #temp.add_section('section')
        #temp.set('section', 'option', 'value')
        #logger.debug("[{}]\n".format('section_name'))
        temp.add_section(TestUtil._section)
        temp.set(TestUtil._section, TestUtil.log_to_file.__name__, TestUtil._log_to_file)
        temp.set(TestUtil._section, TestUtil.log_file_name.__name__, TestUtil._log_file_name)
        temp.set(TestUtil._section, TestUtil.init_testing.__name__, TestUtil._init_testing)
        temp.set(TestUtil._section, TestUtil.run_command_testing.__name__, TestUtil._run_command_testing)
        temp.set(TestUtil._section, TestUtil.logging_testing.__name__, TestUtil._logging_testing)
        temp.set(TestUtil._section, TestUtil.win_only_test.__name__, TestUtil._win_only_test)
        temp.set(TestUtil._section, TestUtil.linux_sudo_test.__name__, TestUtil._linux_sudo_test)

        temp.add_section(TestXml._section)
        temp.set(TestXml._section, TestXml.log_to_file.__name__, TestXml._log_to_file)
        temp.set(TestXml._section, TestXml.log_file_name.__name__, TestXml._log_file_name)
        temp.set(TestXml._section, TestXml.create_sample.__name__, TestXml._create_sample)
        temp.set(TestXml._section, TestXml.overwrite_sample.__name__, TestXml._overwrite_sample)
        temp.set(TestXml._section, TestXml.parse.__name__, TestXml._parse)
        temp.set(TestXml._section, TestXml.init.__name__, TestXml._init)
        temp.set(TestXml._section, TestXml.download.__name__, TestXml._download)
        temp.set(TestXml._section, TestXml.install.__name__, TestXml._install)
        temp.set(TestXml._section, TestXml.configure.__name__, TestXml._configure)

        with open(conffile, 'w') as configfile:
            temp.write(configfile)
            #configfile.write("[{}]\n".format('section_name'))

