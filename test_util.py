'''
Created on 2020-04-13

@author: lordmike
'''

import setup_apps
from setup_apps import util

if __name__ == '__main__':
    print('Init messsage test_util.py')
    print('setup_apps.revision: ' + str(setup_apps.__revision__))

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
    print('')
    print('END')
