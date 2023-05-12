from decouple import config

debug = config("DEBUG", cast=bool)

if debug:
    from .development import *
else:
    from .production import *
