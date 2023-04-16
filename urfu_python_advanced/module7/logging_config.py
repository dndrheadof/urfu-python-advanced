import logging.config
import sys
from urfu_python_advanced.module7.task3 import FileByLevelHandler


class IsASCII(logging.Filter):
    def filter(self, record):
        return str.isascii(record.msg)


config = {
    "version": 1,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s"
        }
    },
    "filters": {"ascii": {"()": IsASCII}},
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "stream": sys.stdout,
            "filters": ["ascii"],
            "formatter": "base",
        },
        "files_by_level": {
            "()": FileByLevelHandler,
            "level": "DEBUG",
            "formatter": "base",
        },
        "time_rotating": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "INFO",
            "formatter": "base",
            "when": "h",
            "interval": 10,
            "backupCount": 1,
            "filename": "utils.log",
        },
    },
    "loggers": {
        "app": {"level": "DEBUG", "handlers": ["console", "files_by_level"]},
        "utils": {"level": "INFO", "handlers": ["time_rotating"]},
    },
}


def configure_logging():
    logging.config.dictConfig(config)
