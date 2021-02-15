'''
Created on 2020-04-13

@author: lordmike
'''

import setup_apps
from setup_apps import util
import sys
import logging
import os
from LMToyBoxPython import LMhashlib
#from setup_apps.util import hint_test
'''
def hint_test(test: str) -> bool:
    return isinstance(test, str)
'''

logger = logging.getLogger('test_util_local')
logger.propagate = False

# TODO: create speed test for  LMhashlib._hash_core(...) and optimize it 

def init_testing():
    logger.info('')
    logger.info('Test function "python_version_str"')
    test = util.python_version_str()
    logger.info('Python version: ' + str(test))

    logger.info('')
    logger.info('Test function "python_version"')
    test = util.python_version()
    logger.info('Python version: ' + str(test))

    # NOTE: This code is tested only with Python version 3.7
    assert sys.version_info >= (3, 7)

    logger.info('')
    logger.info('Test function "hint_test"')
    # TODO: why __annotations__ is marked as error in Eclipse?!
    logger.info('annotations: ' + str(util.hint_test.__annotations__))
    #print('' + str(typing.get_type_hints(util.hint_test)))
    #print('' + str(hint_test.__annotations__))
    logger.info('Call: ' + "hint_test('test')")
    test = util.hint_test('test')
    logger.info('hint_test: ' + str(test))
    logger.info('Call: ' + "hint_test(1)")
    test = util.hint_test(1)
    logger.info('hint_test: ' + str(test))

    logger.info('')
    logger.info('Test function "hint_test_complex"')
    logger.info('annotations: ' + str(util.hint_test_complex.__annotations__))
    logger.info('Call: ' + "hint_test_complex('test')")
    test = util.hint_test_complex('test')
    logger.info('hint_test_complex: ' + str(test))
    logger.info('Call: ' + "hint_test_complex(1)")
    test = util.hint_test_complex(1)
    logger.info('hint_test_complex: ' + str(test))

    logger.info('')
    logger.info('This system is: ' + str(sys.platform))

    logger.info('')
    logger.info('Test function "is_os_windows"')
    test = util.is_os_windows()
    logger.info('This system is Windows: ' + str(test))

    logger.info('')
    logger.info('Test function "is_os_linux"')
    test = util.is_os_linux()
    logger.info('This system is linux: ' + str(test))

    logger.info('')
    logger.info('Test function "pause"')
    util.pause()

    logger.info('')
    logger.info('Test function "home_path"')
    home_dir = util.home_path()
    logger.info('The user home path: ' + str(home_dir))

def win_only_test():
    if not util.is_os_windows():
        return
    src_samba = ''
    dst_drive = 'T:'
    #setup_apps.connect_samba_share(dst_drive=dst_drive)
    util.connect_samba_share(src_samba = '\\\\192.168.122.1\\sambashare\\windows',
                             dst_drive=dst_drive)
    #util.unzip('W:\\spacesniffer_1_3_0_2.zip', 'C:\\temp\\spacesniffer_1_3_0_2')
    #util.move_win('C:\\temp\\spacesniffer_1_3_0_2', 'C:\\temp\\spacesniffer_temp')
    exe_file = 'C:\\temp\\spacesniffer_temp\\SpaceSniffer.exe'
    dst_link_file = os.environ.get('USERPROFILE') + '\\Desktop\\spacesniffer_temp.lnk'
    #util.shortcut(exe_file=exe_file, dst_link_file=dst_link_file, ico='')
    '''
    test = util.msiexec(
        name = 'Putty install TEST',
        installer = 'W:\\putty-64bit-0.73-installer.msi',
        properties = {
            'INSTALLDIR': 'C:\\temp\\putty_temp\\',
            'ACTION': 'INSTALL',
            'ADDLOCAL': 'FilesFeature,DesktopFeature,PathFeature,PPKFeature',
            },
        log_file = 'C:\\temp\\PuttyInstall.log',
        show_progress = True
    )
    '''
    #util.pause()

def run_command_testing():
    logger.info('')
    logger.info('Test function "run_os_command"')
    test = util.run_os_command('echo "TEST"')
    logger.info('Command succeeded: ' + str(test))

    logger.info('')
    logger.info('Test function "run_os_command"')
    test = util.run_os_command('foo')
    logger.info('Command succeeded: ' + str(test))

    logger.info('')
    logger.info('Test function "run_command"')
    command = '"python.exe"'
    command = command + ' --version'
    #test = util.run_command('echo "TEST"')
    test = util.run_command(command)
    logger.info('Command result: ' + str(test))
    logger.info('Command succeeded: ' + str(test.errorlevel == 0))

    logger.info('')
    logger.info('Test function "run_command"')
    #command = '"' + str(PATH_APP_PY38) + '\\python.exe"'
    command = '"' + 'C:\\Program Files\\Python38' + '\\python.exe"'
    command = command + ' --version'
    #test = util.run_command('echo "TEST"')
    test = util.run_command(command)
    logger.info('Command result: ' + str(test))
    logger.info('Command succeeded: ' + str(test.errorlevel == 0))

    logger.info('')
    logger.info('Test function "run_command"')
    test = util.run_command('echo "TEST"')
    logger.info('Command result: ' + str(test))
    logger.info('Command succeeded: ' + str(test.errorlevel == 0))
    logger.info('')
    logger.debug('NOTE: Shell internal command is not available')

    logger.debug('NOTE: without shell "echo" command does not exist')
    logger.info('')
    logger.info('Test function "run_command"')
    test = util.run_command('echo "TEST"', shell=True)
    logger.info('Command result: ' + str(test))
    logger.info('Command succeeded: ' + str(test.errorlevel == 0))

    logger.info('')
    logger.info('Test function "run_command"')
    test = util.run_command('foo', shell=True)
    logger.info('Command result: ' + str(test))
    logger.info('Command succeeded: ' + str(test.errorlevel == 0))

    logger.info('')
    logger.info('Test function "run_command"')
    test = util.run_command('echo "TEST 1" && echo "TEST 2"', shell=True)
    logger.info('Command result: ' + str(test))
    logger.info('Command succeeded: ' + str(test.errorlevel == 0))

    logger.info('')
    logger.info('Test function "run_command"')
    test = util.run_command(['echo', 'TEST 1', '&&', 'echo', 'TEST 2'], shell=True)
    logger.info('Command result: ' + str(test))
    logger.info('Command succeeded: ' + str(test.errorlevel == 0))

    logger.info('')
    logger.info('Test function "run_command_alt_1"')
    test = util.run_command_alt_1(['echo', 'TEST 1', '&&', 'echo', 'TEST 2'])
    logger.info('Command result: ' + str(test))
    logger.info('Command succeeded: ' + str(test.returncode == 0))

    logger.info('')
    logger.info('Test function "run_command_alt_1"')
    test = util.run_command_alt_1(['echo', 'TEST 1', '&&', 'echo', 'TEST 2'], shell=True)
    logger.info('Command result: ' + str(test))
    logger.info('Command succeeded: ' + str(test.returncode == 0))

    logger.info('')
    logger.info('Test function "run_command_alt_1"')
    test = util.run_command_alt_1(['foo'], shell=True)
    logger.info('Command result: ' + str(test))
    logger.info('Command succeeded: ' + str(test.returncode == 0))


def setup_root_logging():
    logging.basicConfig(
        #format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
        #format=None,
        #format='',
        #datefmt='%d.%m.%Y %H:%M:%S',
        #stream=sys.stdout,
        # Parent logger must have INFO level or child logger will not log get INFO level messges
        level=logging.DEBUG
        #level=logging.INFO
        #level=logging.ERROR
        )

def create_logger():
    logger_test_util = logging.getLogger('test_util')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s {%(pathname)s:%(lineno)d}')
    ch = logging.StreamHandler(stream=sys.stdout)
    #ch = logging.FileHandler('logfile_setup_apps.log')
    #ch.setLevel(logging.DEBUG)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger_test_util.addHandler(ch)
    ch_err = logging.StreamHandler(stream=sys.stderr)
    ch_err.setLevel(logging.ERROR)
    ch_err.setFormatter(formatter)
    logger_test_util.addHandler(ch_err)
    # Do not propagate the error up to parent
    logger_test_util.propagate = False
    return logger_test_util

def create_logger_local():
    logger_test = logging.getLogger('test_util_local')
    formatter = logging.Formatter('%(name)s - %(levelname)-5s - %(message)s [%(pathname)s:%(lineno)d]')
    ch = logging.StreamHandler(stream=sys.stdout)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger_test.addHandler(ch)

def create_logger_local_to_file(log_file_name: str):
    logger_test = logging.getLogger('test_util_local')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-5s - %(message)s [%(pathname)s:%(lineno)d]')
    #fh = logging.FileHandler('spam_test_util.log')
    fh = logging.FileHandler(log_file_name)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger_test.addHandler(fh)

def config_logger_setup_apps():
    logger.info('Conf the "setup_apps" at test_util')
    log = logging.getLogger('setup_apps')
    #formatter = logging.Formatter('[test_util conffed] - %(name)s - %(levelname)s - %(message)s')
    formatter = logging.Formatter('%(name)s - %(levelname)-5s - %(message)s [%(pathname)s:%(lineno)d]')
    ch = logging.StreamHandler(stream=sys.stdout)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    log.addHandler(ch)

def config_logger_setup_apps_to_file(log_file_name: str):
    # https://docs.python.org/3/howto/logging-cookbook.html
    logger.info('Conf the "setup_apps" at test_util into file')
    log = logging.getLogger('setup_apps')
    #formatter = logging.Formatter('[test_util conffed] - %(name)s - %(levelname)s - %(message)s')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-5s - %(message)s [%(pathname)s:%(lineno)d]')
    #fh = logging.FileHandler('spam_test_util.log')
    fh = logging.FileHandler(log_file_name)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    log.addHandler(fh)

def logging_testing():
    # https://docs.python.org/3/library/logging.html
    # https://docs.python.org/3/howto/logging.html
    # https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library
    # https://www.loggly.com/ultimate-guide/python-logging-basics/
    # https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler
    # https://www.toptal.com/python/in-depth-python-logging

    setup_root_logging()
    logger_test_util = create_logger()
    logger_test_util.info('INFO log from test_util')
    logger_test_util.error('ERROR log from test_util')
    logging.info('INFO log from "root" logging')
    logging.error('ERROR log from "root" logging')
    config_logger_setup_apps()
    util.logging_test()


if __name__ == '__main__':
    # Always setup logger :)
    setup_root_logging()
    create_logger_local()
    create_logger_local_to_file('spam_test_util.log')
    
    logger.info('Init messsage test_util.py')
    logger.info('setup_apps.revision: ' + str(setup_apps.__revision__))

    # Always setup logger :)
    #setup_root_logging()
    config_logger_setup_apps()
    config_logger_setup_apps_to_file('spam_test_util.log')

    init_testing()
    #run_command_testing()
    #logging_testing()
    win_only_test()

    logger.info('')
    logger.info('')
    logger.info('END')
