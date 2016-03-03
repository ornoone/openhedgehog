#!/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'darius BERNARD <darius@xornot.fr>'

from .common import *
import os
import logging
logger = logging.getLogger(__name__)



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = False


ALLOWED_HOSTS = []
