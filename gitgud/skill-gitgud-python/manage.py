#!/usr/bin/env python
from skill_sdk.manage import manage
import os
import configparser


conf_file = 'skill.conf'

if 'PORT' in os.environ:
    config = configparser.ConfigParser()
    config.read(conf_file)
    config['http']['port'] = os.environ['PORT']
    with open(conf_file, 'w') as configfile:
        config.write(configfile)
    print(config['http']['port'])    
print(config['http']['port'])     


manage()
