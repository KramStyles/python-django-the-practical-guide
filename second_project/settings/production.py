from second_project.settings.base import *

ALLOWED_HOSTS.append(config("ALLOWED_HOSTS"))
SECRET_KEY = config("SECRET_KEY")
