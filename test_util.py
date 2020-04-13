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
    print('')
    print('END')
