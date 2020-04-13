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
    test = util.run_command('echo "TEST"')
    print('Command result: ' + str(test))

    print('')
    print('')
    print('END')
