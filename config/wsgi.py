"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
>>>>>>> b13309c0958af968b4ece0ec77164443d9e852c4

application = get_wsgi_application()
