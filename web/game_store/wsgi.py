"""
WSGI config for game_store project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import pathlib
import dotenv

from django.core.wsgi import get_wsgi_application

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
print(BASE_DIR)
ENV_PATH = BASE_DIR / ".env"
dotenv.read_dotenv(str(ENV_PATH))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'game_store.settings')

application = get_wsgi_application()
