#!/home3/tzeppyco/python/bin/python

from flup.server.fcgi import WSGIServer
from app import app as application

WSGIServer(application).run()

