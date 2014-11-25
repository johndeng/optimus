# coding: utf-8

from tests.base import BaseHTTPTestCase


class HelloTest(BaseHTTPTestCase):

    def setUp(self):
        super(HelloTest, self).setUp()


    def test_visit_hello(self):
        r = self.get('/')
        self.assertEqual("Hello World!", r.body)

    def test_post_hello(self):
        r = self.post('/', body='')
        self.assertEqual("Hello World!", r.body)
