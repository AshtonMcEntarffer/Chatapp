"""
WSGI config for chat project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append('/root/Chatapp')


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chat.settings")


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
