site_name = 'snakeoil'

# command = '/srv/{}/venv/bin/gunicorn'.format(site_name)
command = '/home/ubuntu/.local/bin/gunicorn'
python = '/srv/{}'.format(site_name)
bind = '127.0.0.1:8001'

preload_app = True
workers = 3