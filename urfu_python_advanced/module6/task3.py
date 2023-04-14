import json
import logging


class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        msg = json.dumps(msg, ensure_ascii=False)
        return msg, kwargs


logging.basicConfig(
    level=logging.INFO,
    filename="messages.log",
    format='{"time": "%(asctime)s", "level": "%(levelname)s", "message": %(message)s}',
    datefmt="%H:%M:%S",
)


logger = JsonAdapter(logging.getLogger(__name__))
logger.info("Сообщение")
