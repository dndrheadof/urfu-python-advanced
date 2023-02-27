from flask import Flask
from random import choice
from datetime import datetime, timedelta
import os
import re

app = Flask(__name__)
CARS = ["Chevrolet", "Renault", "Ford", "Lada"]
CATS = ["корниш-рекс", "русская голубая",
        "шотландская вислоухая", "мейн-кун", "манчкин"]
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, "war-and-peace.txt")
COUNTER = 0

with open(BOOK_FILE, encoding="windows-1251") as file:
    words = re.findall("\w+", file.read(), flags=re.IGNORECASE)


@app.route("/hello_world")
def hello_world():
    return "Привет, мир!"


@app.route("/cars")
def cars():
    return ", ".join(CARS)


@app.route("/cats")
def cats():
    return f"Случайная порода кошки: {choice(CATS)}"


@app.route("/get_time/now")
def time_now():
    current_time = datetime.now()
    return f"Точное время: {current_time}"


@app.route("/get_time/future")
def time_future():
    current_time_after_hour = datetime.now() + timedelta(hours=1)
    return f"Точное время через час будет {current_time_after_hour}"


@app.route("/get_random_word")
def random_word():
    word = choice(words)
    return f"Случайное слово: {word}"


@app.route("/counter")
def counter():
    global COUNTER
    COUNTER += 1
    return f"Количество посещений: {COUNTER}"


if __name__ == "__main__":
    app.run()
