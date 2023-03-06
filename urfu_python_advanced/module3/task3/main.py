from flask import Flask
from datetime import datetime

app = Flask(__name__)

expenses = {
    2022: {
        12: {
            31: 123
        },
        11: {
            12: 122,
            14: 1331
        }
    },
    2023: {
        2: {
            27: 1279
        }
    }
}


@app.route('/add/<date>/<int:number>')
def add_expense(date, number):
    try:
        date = datetime.strptime(date, "%Y%m%d")

        expenses.setdefault(date.year, {}).setdefault(
            date.month, {}).setdefault(date.day, 0)

        expenses[date.year][date.month][date.day] += number
        return expenses
    except ValueError:
        raise ValueError("Ошибка: дата должна быть в формате YYYYMMDD")


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
