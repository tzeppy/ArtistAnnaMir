#!/usr/bin/env python

import logging
from app import app
from views import all

log = logging.getLogger(__name__)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(threaded=True)

