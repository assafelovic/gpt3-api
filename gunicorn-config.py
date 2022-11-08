# -*- encoding: utf-8 -*-
from api.config import PORT

bind = '0.0.0.0:{0}'.format(PORT)
workers = 2
accesslog = '-'
loglevel = 'debug'
capture_output = True
enable_stdio_inheritance = True