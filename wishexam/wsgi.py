# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
WSGI config for Wish_BeltExam project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wishexam.settings")

application = get_wsgi_application()
