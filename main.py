#! /usr/bin/env python

import logging

log = logging.getLogger(__name__)

if __name__=="__main__":
    from optparse import OptionParser
    import sys
    from app import app
    from views import all
    #
    usage = "usage: %s [--port 5000] [--debugLevel INFO] [--localonly]" % (sys.argv[0])
    parser = OptionParser(usage=usage)
    parser.add_option("-p", "--port", type="int", default=5000)
    parser.add_option("-d", "--debug", action="store_const", const=logging.DEBUG, default=logging.INFO)
    #
    options, args = parser.parse_args()
    #
    myhost = "0.0.0.0"
    logging.basicConfig(level=options.debug)
    app.run(host=myhost, port=options.port, debug=True, threaded=True)
