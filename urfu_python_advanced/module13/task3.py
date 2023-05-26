import datetime
import sqlite3


def log_bird(
    cursor: sqlite3.Cursor,
    bird_name: str,
    date_time: str,
) -> None:
    if not check_if_such_bird_already_seen(cursor, bird_name):
        cursor.execute(
            "insert into table_birds (name, timestamp) values (?, ?)",
            (bird_name, date_time),
        )


def check_if_such_bird_already_seen(cursor: sqlite3.Cursor, bird_name: str) -> bool:
    cursor.execute(
        "select exists (select * from table_birds where name=?)", (bird_name)
    )
    return bool(cursor.fetchone()[0])


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()

        cursor.execute(
            """create table if not exists table_birds(
                            id integer primary key autoincrement,
                            name varchar(100) not null,
                            timestamp datatime(100) not null)"""
        )

        conn.commit()

        log_bird(cursor, "ptica", str(datetime.datetime.now()))
