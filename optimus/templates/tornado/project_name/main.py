#!/usr/bin/env python
# coding: utf-8

import os
import sys

_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(_root)

import tornado.web
import tornado.options
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

import urls
import settings


define("port", default=8000, help="Run on the given port", type=int)


def app():
    return tornado.web.Application(urls.handlers,
                                   **settings.APP_SETTINGS)


def main():

    # disable tornado's logging
    options.logging = None
    tornado.options.parse_command_line()

    # using our own logging config
    from log_settings import define_logging
    define_logging()

    http_server = tornado.httpserver.HTTPServer(app())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
