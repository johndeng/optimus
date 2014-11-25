# coding: utf-8

import unittest
import tornado.testing

from glob import glob


def all():
    tests = map(lambda x: x.rstrip('.py').replace('/', '.'),
                glob('tests/test_*.py'))
    test_modules = map(lambda x: x.rstrip('.py').replace('/', '.'),
                       glob('tests/**/*.py'))
    test_modules.extend(tests)
    return unittest.defaultTestLoader.loadTestsFromNames(test_modules)

if __name__ == '__main__':

    tornado.testing.main()
