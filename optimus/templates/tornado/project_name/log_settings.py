# coding: utf-8

"""
    logging settings
    ~~~~~~~~~~~~~~~~

    log config

"""


def define_logging(level='info'):

    import logging

    logger = logging.getLogger()
    logger.setLevel(getattr(logging, level.upper()))
    channel = logging.StreamHandler()
    channel.setFormatter(
        logging.Formatter(
            "[%(levelname)s %(asctime)s "
            "%(processName)s %(filename)s - %(funcName)s - %(lineno)d] "
            "%(message)s")
    )
    logger.addHandler(channel)
