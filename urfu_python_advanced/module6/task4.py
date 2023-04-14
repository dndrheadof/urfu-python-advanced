import itertools
import json
from collections import Counter


def count_logs_by_level(logs):
    for level, log_group in itertools.groupby(
        sorted(logs, key=lambda j: j["level"]), key=lambda j: j["level"]
    ):
        print(f"{level}: {len(list(log_group))}")


def max_logs_by_hour(logs):
    logs_by_hour = {}
    for hour, log_group in itertools.groupby(
        logs, key=lambda j: j["time"].split(":")[0]
    ):
        logs_by_hour[hour] = len(list(log_group))
    print(f"Больше всего логов в {max(logs_by_hour, key=logs_by_hour.get)} час")


def count_critical_logs(logs):
    critical = [
        log
        for log in logs
        if "05:00:00" <= log["time"] <= "05:20:00" and log["level"] == "CRITICAL"
    ]
    print(f"Количество критических логов с 05:00:00 до 05:20:00: {len(critical)}")


def count_logs_with_dog(logs):
    found = [log for log in logs if "dog" in log["message"]]
    print(f"Сообщений с dog: {len(found)}")


def most_frequent_word_in_warning(logs):
    warnings = [log["message"] for log in logs if log["level"] == "WARNING"]
    words = [word for word in (warning.split() for warning in warnings)]

    # https://stackoverflow.com/questions/3594514/how-to-find-most-common-elements-of-a-list
    most_frequent, count = Counter(
        [item for sublist in words for item in sublist]
    ).most_common(1)[0]

    print(f"Самое частое слово: {most_frequent}, кол-во раз: {count}")


with open("messages.log", "r") as F:
    logs = [json.loads(line) for line in F.readlines()]

count_logs_by_level(logs)
max_logs_by_hour(logs)
count_critical_logs(logs)
count_logs_with_dog(logs)
most_frequent_word_in_warning(logs)
