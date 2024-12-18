from .settings import *
from dotenv import load_dotenv
import os

load_dotenv()

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0', 'localhost']

X_FRAME_OPTIONS = 'localhost'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # 'TEST': {
        #     'MIRROR': 'default'
        # },
        'NAME': os.getenv('DJANGO_DATABASE_NAME'),
        'USER': os.getenv('DJANGO_DATABASE_USER'),
        'PASSWORD': os.getenv('DJANGO_DATABASE_PASSWORD'),
        'HOST': 'rcs_database',
        'PORT': '5432',
    }
}
