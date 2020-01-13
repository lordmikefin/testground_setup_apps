'''
Created on 11 Jan 2020

@author: lordmike
'''

import setup_apps

if __name__ == '__main__':
    print('Init messsage test_xml.py')
    print('setup_apps.revision: ' + str(setup_apps.__revision__))
    #setup_apps.config.read_write()
    #setup_apps.config.create_test_xml()
    setup_apps.config.create_sample()
    setup_apps.config.print_sample()
    setup_apps.config.parse()
    print('END')
