![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Django Rest Framework](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![Vue.js](https://img.shields.io/badge/vuejs-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white)

# Social Membership app using Django and React

This is a social membership app written in Python, Django and Django Rest Framework. This also uses Vue JS for some front-end use cases.
This social membership app has a multi-level marketing model and has incensitives based on the level of the user for each sell made.

## Deployment using Gunicorn

Install Guvicorn server 

```
pip install gunicorn
```

Create a Gunicorn.conf.py file in the root folder

```
import os

bind = os.environ.get('BIND', '0.0.0.0:8000')
workers = os.environ.get('WORKERS', 3)  # Adjust as needed
logfile = os.environ.get('LOGFILE', '/path/to/gunicorn.log')
loglevel = os.environ.get('LOGLEVEL', 'info')

# Point to your Django application's WSGI entry point
wsgi_app = 'social_membership.wsgi:application'

```

Run the application

```
gunicorn --config gunicorn.conf.py social_membership.wsgi:application
```

Additional Considerations:

Static Files: Gunicorn primarily serves your Django application. You'll need a separate server like Nginx to handle static files (CSS, JavaScript, images) efficiently. Configure Nginx to act as a reverse proxy, forwarding requests to Gunicorn for dynamic content and serving static files directly.
HTTPS: Implement HTTPS for secure communication in production. Use a tool like Let's Encrypt to obtain SSL certificates.
Process Management: Consider using a process manager like systemd or Supervisord to manage Gunicorn as a service, ensuring it automatically restarts on crashes or system reboots.
