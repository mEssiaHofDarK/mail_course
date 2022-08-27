bind = '0.0.0.0:8000'

workers = 1
worker_class = 'sync'
worker_connections = 100
timeout = 30
keepalive = 2
pythonpath = '/home/box/web/ask'
# pythonpath = '/home/artem/Projects/Python/mail_corse/mail_course/web/ask'
errorlog = '-'
loglevel = 'info'
accesslog = '-'
