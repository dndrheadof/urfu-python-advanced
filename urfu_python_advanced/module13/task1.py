import sqlite3

with sqlite3.connect("hw.db") as conn:
    cursor = conn.cursor()


def check_if_vaccine_has_spoiled(cursor: sqlite3.Cursor, truck_number: str) -> bool:
    cursor.execute(
        f"select * from table_truck_with_vaccine where truck_number = ? and temperature_in_celsius not between 16 and 20",
        truck_number,
    )
    result = cursor.fetchall()
    return True if len(result) >= 3 else False


print(check_if_vaccine_has_spoiled(cursor, "н289ом78"))
print(check_if_vaccine_has_spoiled(cursor, "о411кр47"))
print(check_if_vaccine_has_spoiled(cursor, "т153ет78"))
print(check_if_vaccine_has_spoiled(cursor, "с253ка48"))
