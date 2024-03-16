"""
ASGI config for content_detection_and_classification_of_youtube_videos.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'content_detection_and_classification_of_youtube_videos.settings')

application = get_asgi_application()
