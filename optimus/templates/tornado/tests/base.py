# coding: utf-8

import unittest
from urllib import urlencode

from tornado.testing import AsyncHTTPTestCase as TornadoAsyncTestCase
from {{ project_name }}.main import app


class BaseHTTPTestCase(TornadoAsyncTestCase):
    """
    Test care base.
    """
    def get_app(self):
        self.app = app()
        return self.app

    def get(self, url, **kwargs):
        return self.fetch(url, **kwargs)

    def post(self, url, **kwargs):
        if 'body' in kwargs and isinstance(kwargs['body'], dict):
            kwargs['body'] = urlencode(kwargs['body'])
        return self.fetch(url, method="POST", **kwargs)

    def delete(self, url, **kwargs):
        return self.fetch(url, method="DELETE", **kwargs)


class BaseTestCase(unittest.TestCase):
    pass
