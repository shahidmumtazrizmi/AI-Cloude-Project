import sys
import os

# Add the project directory to the sys.path
sys.path.insert(0, os.path.dirname(__file__))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cloudai_platform.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application() 