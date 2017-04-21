#!/usr/bin/python

import sys
import logging
loggin.pasicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/cs329e-idb/")


from app import app as application
application.secret_key = 'Add your secret key'

