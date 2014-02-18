#!/bin/bash

exec uwsgi -H mtg --no-site --loop gevent --http-socket :9000 --module mtgapi.wsgi --async 1000
