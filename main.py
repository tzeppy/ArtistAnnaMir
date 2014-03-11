#!/usr/bin/env python

from app import app
from views import all

if __name__ == '__main__':
    app.run(threaded=True)

