from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)

GREETINGS = ('Хорошего понедельника!', 'Хорошего вторника!',
             'Хорошей среды!', 'Хорошего четверга!', 'Хорошей пятницы!', 'Хорошей субботы!', 'Хорошего воскресенья!')

expenses = {}


@app.route("/hello-world/<name>")
def hello_world(name: str):
    weekday = datetime.today().weekday()
    greeting = GREETINGS[weekday]
    return f"Привет, {name}! {greeting}"


@app.route("/max_number/<path:numbers>")
def max_number(numbers: str):
    numbers = list(filter(None, numbers.split('/')))
    if all(i.isdigit() for i in numbers):
        return f"Максимальное число: <i>{max(map(int, numbers))}</i>"
    return "В списке присутствуют не числа"


@app.route("/<path:file_path>")
@app.route("/preview/<int:size>/<path:file_path>")
def get_file_preview(file_path, size=-1):
    abs_path = os.path.abspath(file_path)
    file = open(abs_path, 'r')
    file_contents = file.read(size)

    file.close()
    return f"<b>{abs_path}</b> {len(file_contents)}<br>{file_contents}"


@app.route('/add/<date>/<int:number>')
def add_expense(date, number):
    date = datetime.strptime(date, "%Y%m%d")

    expenses.setdefault(date.year, {}).setdefault(
        date.month, {}).setdefault(date.day, 0)

    expenses[date.year][date.month][date.day] += number
    return expenses


@app.route("/calculate/<int:year>")
def calculate_year(year):
    if not year in expenses:
        return "Данного года не существует в хранилище"

    return f"Сумма трат за {year} год: {sum([sum([day for day in month.values()]) for month in expenses[year].values()])}"


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year, month):
    if not year in expenses or not month in expenses[year]:
        return "Данного года/месяца не существует в хранилище"

    return f"Сумма трат за {month} месяц {year} года: {sum([day for day in expenses[year][month].values()])}"


if __name__ == "__main__":
    app.run(debug=True)
