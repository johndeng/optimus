# coding: utf-8


from {{ project_name }}.handlers.hello import HelloHandler

handlers = [
    (r'/', HelloHandler),
]
