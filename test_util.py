'''
Created on 2020-04-13

@author: lordmike
'''

import setup_apps
from setup_apps import util
import sys
import logging
#from setup_apps.util import hint_test
'''
def hint_test(test: str) -> bool:
    return isinstance(test, str)
'''


#logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.ERROR)
#logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.basicConfig(
    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
    #format=None,
    #format='',
    datefmt='%d.%m.%Y %H:%M:%S',
    stream=sys.stdout,
    # Parent logger must have INFO level or child logger will not log get INFO level messges
    level=logging.INFO
    #level=logging.ERROR
    )


#logging.getLogger().addHandler(logging.NullHandler())
#logging.getLogger('setup_apps').addHandler(logging.NullHandler())
#logging.getLogger('root').addHandler(logging.NullHandler())

#logger_root = logging.getLogger('root')
logger_root = logging.getLogger()
#ch_root = logging.StreamHandler()
#ch_root = logging.StreamHandler(stream=sys.stdout)
#ch_root = logging.FileHandler('logfile_root.log')
ch_root = logging.StreamHandler(stream=sys.stderr)
#ch_root.setLevel(logging.INFO)
ch_root.setLevel(logging.ERROR)
formatter_root = logging.Formatter('ROOT - %(name)s - %(levelname)s - %(message)s')
ch_root.setFormatter(formatter_root)
logger_root.addHandler(ch_root)
# Do not propagate the error up to parent
logger_root.propagate = False


logger_setup_apps = logging.getLogger('setup_apps')
#ch = logging.StreamHandler()
ch = logging.StreamHandler(stream=sys.stdout)
#ch = logging.FileHandler('logfile_setup_apps.log')
#ch.setLevel(logging.DEBUG)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger_setup_apps.addHandler(ch)
ch_err = logging.StreamHandler(stream=sys.stderr)
ch_err.setLevel(logging.ERROR)
ch_err.setFormatter(formatter)
logger_setup_apps.addHandler(ch_err)
# Do not propagate the error up to parent
#logger_setup_apps.propagate = False

#logger_setup_apps.addHandler(logging.NullHandler())


def init_testing():
    print('')
    print('Test function "python_version_str"')
    test = util.python_version_str()
    print('Python version: ' + str(test))

    print('')
    print('Test function "python_version"')
    test = util.python_version()
    print('Python version: ' + str(test))

    # NOTE: This code is tested only with Python version 3.7
    assert sys.version_info >= (3, 7)

    print('')
    print('Test function "hint_test"')
    # TODO: why __annotations__ is marked as error in Eclipse?!
    print('annotations: ' + str(util.hint_test.__annotations__))
    #print('' + str(typing.get_type_hints(util.hint_test)))
    #print('' + str(hint_test.__annotations__))
    print('Call: ' + "hint_test('test')")
    test = util.hint_test('test')
    print('hint_test: ' + str(test))
    print('Call: ' + "hint_test(1)")
    test = util.hint_test(1)
    print('hint_test: ' + str(test))

    print('')
    print('Test function "hint_test_complex"')
    print('annotations: ' + str(util.hint_test_complex.__annotations__))
    print('Call: ' + "hint_test_complex('test')")
    test = util.hint_test_complex('test')
    print('hint_test_complex: ' + str(test))
    print('Call: ' + "hint_test_complex(1)")
    test = util.hint_test_complex(1)
    print('hint_test_complex: ' + str(test))

    print('')
    print('Test function "is_os_windows"')
    test = util.is_os_windows()
    print('This system is Windows: ' + str(test))

    print('')
    print('Test function "pause"')
    util.pause()

    print('')
    print('Test function "home_path"')
    home_dir = util.home_path()
    print('The user home path: ' + str(home_dir))


def run_command_testing():
    print('')
    print('Test function "run_os_command"')
    test = util.run_os_command('echo "TEST"')
    print('Command succeeded: ' + str(test))

    print('')
    print('Test function "run_os_command"')
    test = util.run_os_command('foo')
    print('Command succeeded: ' + str(test))

    print('')
    print('Test function "run_command"')
    command = '"python.exe"'
    command = command + ' --version'
    #test = util.run_command('echo "TEST"')
    test = util.run_command(command)
    print('Command result: ' + str(test))

    print('')
    print('Test function "run_command"')
    #command = '"' + str(PATH_APP_PY38) + '\\python.exe"'
    command = '"' + 'C:\\Program Files\\Python38' + '\\python.exe"'
    command = command + ' --version'
    #test = util.run_command('echo "TEST"')
    test = util.run_command(command)
    print('Command result: ' + str(test))

    print('')
    print('Test function "run_command"')
    test = util.run_command('echo "TEST"')
    print('Command result: ' + str(test))
    print('')
    print('NOTE: Shell internal command is not available')

    print('')
    print('NOTE: without shell "echo" command does not exist')
    print('')
    print('Test function "run_command"')
    test = util.run_command('echo "TEST"', shell=True)
    print('Command result: ' + str(test))

    print('')
    print('Test function "run_command"')
    test = util.run_command('foo', shell=True)
    print('Command result: ' + str(test))

    print('')
    print('Test function "run_command"')
    test = util.run_command('echo "TEST 1" && echo "TEST 2"', shell=True)
    print('Command result: ' + str(test))

    print('')
    print('Test function "run_command"')
    test = util.run_command(['echo', 'TEST 1', '&&', 'echo', 'TEST 2'], shell=True)
    print('Command result: ' + str(test))

    print('')
    print('Test function "run_command_alt_1"')
    test = util.run_command_alt_1(['echo', 'TEST 1', '&&', 'echo', 'TEST 2'])
    print('Command result: ' + str(test))

    print('')
    print('Test function "run_command_alt_1"')
    test = util.run_command_alt_1(['echo', 'TEST 1', '&&', 'echo', 'TEST 2'], shell=True)
    print('Command result: ' + str(test))

    print('')
    print('Test function "run_command_alt_1"')
    test = util.run_command_alt_1(['foo'], shell=True)
    print('Command result: ' + str(test))


def logging_call():
    print('local logging')
    #logging.info('INFO log from test_util')
    #logging.error('ERROR log from test_util')
    logger_root.info('INFO log from test_util')
    logger_root.error('ERROR log from test_util')

    print('logging_test()')
    util.logging_test()

def logging_disable():
    print('')
    print('Init')
    logging_call()
    print('')
    print('Disable "root" logger')
    # NOTE: looks like 'root' logger can not be disabled ?!
    #logging.getLogger('root').addHandler(logging.NullHandler())
    logging.getLogger().addHandler(logging.NullHandler())
    logging_call()
    print('')
    print('Disable "setup_apps" logger')
    logging.getLogger('setup_apps').addHandler(logging.NullHandler())
    logging_call()
    # NOTE: All errors are logged always in the 'root' ?!

def logging_info():
    print('')
    print('Basic logging level INFO')
    logging.basicConfig(level=logging.INFO)
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    print('')
    print('Init')
    logging_call()

def logging_testing():
    # https://docs.python.org/3/library/logging.html
    # https://docs.python.org/3/howto/logging.html
    # https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library
    # https://www.loggly.com/ultimate-guide/python-logging-basics/
    # https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler
    # https://www.toptal.com/python/in-depth-python-logging

    # NOTE: Can not configure logger within functions ???
    logging_disable()
    logging_info()
    print('logging logger_setup_apps')
    logger_setup_apps.info('INFO log from logger_setup_apps')
    logger_setup_apps.error('ERROR log from logger_setup_apps')


if __name__ == '__main__':
    print('Init messsage test_util.py')
    print('setup_apps.revision: ' + str(setup_apps.__revision__))

    #init_testing()
    #run_command_testing()
    logging_testing()

    print('')
    print('')
    print('END')
