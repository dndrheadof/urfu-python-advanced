from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)

GREETINGS = ('Хорошего понедельника!', 'Хорошего вторника!',
             'Хорошей среды!', 'Хорошего четверга!', 'Хорошей пятницы!', 'Хорошей субботы!', 'Хорошего воскресенья!')


@app.route("/hello-world/<name>")
def hello_world(name: str):
    weekday = datetime.today().weekday()
    greeting = GREETINGS[weekday]
    return f"Привет, {name}! {greeting}"
