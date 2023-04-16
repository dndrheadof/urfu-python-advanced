import sqlite3

with sqlite3.connect("hw_3_database.db") as conn:
    cursor = conn.cursor()
    # region subtask_1
    cursor.execute("select count(id) from table_1")
    result = cursor.fetchall()
    print(result)  # 50 записей в таблице
    # endregion

    # region subtask_2
    cursor.execute("select count(distinct value) from table_1")
    result = cursor.fetchall()
    print(result)  # 25 уникальных записей
    # endregion

    # region subtask_3
    cursor.execute(
        """select count(value) from (
            select value from table_1
            intersect
            select value from table_2
        )"""
    )
    result = cursor.fetchall()
    print(result)  # 18 значений из table_1 есть в table_2
    # endregion

    # region subtask_4
    cursor.execute(
        """select count(value) from (
            select value from table_1
            intersect
            select value from table_2
            intersect
            select value from table_3
        )"""
    )
    result = cursor.fetchall()
    print(result)  # 12 значений из table_1 есть в table_2 и table_3
    # endregion
