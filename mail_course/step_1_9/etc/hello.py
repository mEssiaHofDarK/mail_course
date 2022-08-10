# """
# https://github.com/benoitc/gunicorn/blob/master/examples/example_config.py
# config description
# """

bind = '0.0.0.0:8080'

workers = 1
worker_class = 'sync'
worker_connections = 100
timeout = 30
keepalive = 2

errorlog = '-'
loglevel = 'info'
accesslog = '-'
