'''
Created on 2020-04-13

@author: lordmike
'''

import setup_apps
from setup_apps import util
import sys
#from setup_apps.util import hint_test
'''
def hint_test(test: str) -> bool:
    return isinstance(test, str)
'''

if __name__ == '__main__':
    print('Init messsage test_util.py')
    print('setup_apps.revision: ' + str(setup_apps.__revision__))

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
    print('')
    print('END')
