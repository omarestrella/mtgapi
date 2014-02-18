"""
WSGI config for mtgapi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

from gevent import monkey
monkey.patch_all()

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mtgapi.settings")

from dj_static import Cling

from django.core.wsgi import get_wsgi_application
application = Cling(get_wsgi_application())
