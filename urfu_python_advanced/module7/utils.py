import logging
from logging_config import configure_logging

logger = logging.getLogger("utils")
configure_logging()


def get_number(message="Введите число: "):
    try:
        number = float(input(message))
        return number
    except ValueError:
        logger.error("Введено не число")
        exit()


def plus(a, b):
    result = a + b
    logger.debug(f"plus {result}")
    return result


def subtract(a, b):
    result = a - b
    logger.debug(f"subtract {result}")
    return result


def multiply(a, b):
    result = a * b
    logger.debug(f"multiply {result}")
    return result


def divide(a, b):
    try:
        result = a / b
        logger.debug(f"divide {result}")
        return result
    except ZeroDivisionError:
        logger.warning("деление на 0")
