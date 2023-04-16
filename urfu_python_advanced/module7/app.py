import logging
from logging_config import configure_logging
import utils
import logging_tree

logger = logging.getLogger("app")

configure_logging()


def calculate():
    logger.debug("ÎŒØ∏‡°⁄·°€йцукен")
    logger.debug("should be visible in logs")
    operation = input("Выберите операцию: '+', '-', '*', '/': ")
    operations = {
        "+": utils.plus,
        "-": utils.subtract,
        "*": utils.multiply,
        "/": utils.divide,
    }
    if operation not in operations:
        logger.error(f"Выбрана неверная операция: {operation}")
        exit()

    a = utils.get_number()
    logger.debug(f"Число 1: {a}")
    b = utils.get_number()
    logger.debug(f"Число 2: {b}")

    result = operations[operation](a, b)
    logger.info(f"a={a}, b={b}, операция: '{operation}', результат: {result}")
    return result


if __name__ == "__main__":
    print(calculate())

    with open("logging_tree.txt", "w") as file:
        file.write(logging_tree.format.build_description())
