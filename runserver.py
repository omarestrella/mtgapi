#!/usr/bin/env python

import sys

from socketio.server import SocketIOServer

from mtgapi.wsgi import application

import werkzeug.serving


@werkzeug.serving.run_with_reloader
def runserver():
    port = 9000
    print 'Listening on http://127.0.0.1:%s and on port 843 (flash policy server)' % port
    SocketIOServer(('', port), application, resource="socket.io").serve_forever()

if __name__ == '__main__':
    runserver()
