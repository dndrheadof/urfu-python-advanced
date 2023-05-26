import sqlite3

with sqlite3.connect("hw.db") as conn:
    cursor = conn.cursor()
    salary = cursor.execute(
        """select salary from `table_effective_manager` where name='Иван Совин'"""
    ).fetchone()[0]


def ivan_sovin_the_most_effective(
    cursor: sqlite3.Cursor,
    name: str,
) -> None:
    cursor.execute(
        """update `table_effective_manager` set salary= 
                      (select salary from `table_effective_manager` where name=?) * 1.1
                      where name=?""",
        (name, name),
    )

    cursor.execute(
        """delete from `table_effective_manager` where name=? and salary>?""",
        (name, salary),
    )


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        ivan_sovin_the_most_effective(cursor, "Михайлов В.Р.")
