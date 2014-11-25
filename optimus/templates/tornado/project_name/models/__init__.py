# coding: utf-8

"""
    {{ project_name }}.models
    ~~~~~~~~~~~~~

    定义模型时, 需要引入base.py里面的两个基类, 分别是: `Sessionized`, `Base`.

    Example::
        from sqlalchemy import Column, String
        from .base import Base, Sessionized

        class ExampleModels(Sessionized, Base):

            test_field = Column(String(255))

    定义完成后, 需要在__init__.py 引入模型, 保证同步生成对应表结构的函数有效.

    Example::
        from .example import ExampleModels

        __all__ = [
            "..",
            "ExampleModels"
        ]

"""
