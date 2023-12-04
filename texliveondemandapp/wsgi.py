from gevent.pywsgi import WSGIServer
from texliveondemand import app

http_server = WSGIServer(('0.0.0.0', 5001), app)
http_server.serve_forever()
