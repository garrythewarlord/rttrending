from .base import *
import os 

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = ['localhost', '46.101.109.199']
STATIC_ROOT = BASE_DIR / "staticfiles"