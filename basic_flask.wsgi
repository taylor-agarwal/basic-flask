import sys
import logging

logging.basicConfig(
	level=logging.DEBUG,
	filename='/var/www/html/basic-flask/logs/basic_flask.log',
	format='%(asctime)s %(message)s'
)
sys.path.insert(0, '/var/www/html/basic-flask')
sys.path.insert(0, '/var/www/html/basic-flask/basic_flask_env/lib/python3.10/site-packages')
from basic_app import app as application
