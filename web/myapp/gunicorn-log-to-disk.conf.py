# Gunicorn config variables
loglevel = "info"
errorlog = "/var/log/gunicorn/error.log"
accesslog = "/var/log/gunicorn/access.log"
worker_tmp_dir = "/dev/shm"
graceful_timeout = 120
timeout = 120
keepalive = 5
threads = 3
bind = "0.0.0.0:8000"
statsd_host = "statsd-exporter:9125"
statsd_prefix = "myapp"
