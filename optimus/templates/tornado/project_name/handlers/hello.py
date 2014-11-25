# coding: utf-8


from {{ project_name }}.handlers import BaseHandler


class HelloHandler(BaseHandler):
    """ For testing project
    """

    def get(self):
        self.handler_logger.info("info")
        self.handler_logger.error("error")
        self.write("Hello World!")

    def post(self):
        self.write("Hello World!")
