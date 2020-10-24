from unbox.settings.base import *

#Override base.py settings here

DEBUG = False

try:
    from unbox.settings.local import *
except:
    pass