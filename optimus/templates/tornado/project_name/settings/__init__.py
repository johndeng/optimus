# coding: utf-8

"""
    settings
    ~~~~~~~~
    project settings

"""

import os
from urlparse import urljoin
from importlib import import_module

PROJECT_PATH = os.path.dirname(__file__)

APP_SETTINGS = {
    "static_path": os.path.join(PROJECT_PATH, 'static'),
    "template_path": os.path.join(PROJECT_PATH, 'templates')
}

DATABASE_USER = ""
DATABASE_PW = ""
DATABASE_HOST = ""
DATABASE_PORT = ""
DATABASE_NAME = ""


debug = os.environ.get("DEBUG", None)

if not debug:
    globals().update(vars(
        import_module("{{ project_name }}.settings.production")
    ))

else:
    globals().update(vars(
        import_module("{{ project_name }}.settings.test")
    ))
