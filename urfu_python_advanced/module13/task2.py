import csv
import sqlite3


def delete_wrong_fees(cursor: sqlite3.Cursor, wrong_fees_file: str) -> None:
    with open(wrong_fees_file, "r", encoding="windows-1251") as file:
        reader = csv.reader(file, delimiter=" ")
        next(reader)
        for row in reader:
            row = row[0].split(",")
            try:
                cursor.execute(
                    "delete from table_fees where truck_number = ? and timestamp = ?",
                    (row[0], row[1]),
                )
            except Exception as e:
                print(e)


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()

        delete_wrong_fees(cursor, "wrong_fees.csv")
