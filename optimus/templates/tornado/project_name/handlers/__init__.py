# coding: utf-8


import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    """ base handler for handler.
    """

    import logging
    handler_logger = logging.getLogger("{{ project_name }}.handler")
