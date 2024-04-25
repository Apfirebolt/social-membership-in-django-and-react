import os

bind = os.environ.get('BIND', '0.0.0.0:8000')
workers = os.environ.get('WORKERS', 3)  # Adjust as needed
logfile = os.environ.get('LOGFILE', '/path/to/gunicorn.log')
loglevel = os.environ.get('LOGLEVEL', 'info')

# Point to your Django application's WSGI entry point
wsgi_app = 'social_membership.wsgi:application'
