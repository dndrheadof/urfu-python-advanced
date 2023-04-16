import sqlite3

with sqlite3.connect("hw_4_database.db") as conn:
    cursor = conn.cursor()
    # region subtask_1
    cursor.execute("select count(id) from salaries where salary < 5000")
    result = cursor.fetchall()
    print(result)  # 27 жителей находятся за чертой бедности
    # endregion

    # region subtask_2
    cursor.execute("select avg(salary) from salaries")
    result = cursor.fetchall()
    print(result)  # средняя зарплата - 9483.36
    # endregion

    # region subtask_3
    cursor.execute(
        """
            SELECT salary
            FROM salaries
            ORDER BY salary
            LIMIT 1
            OFFSET (SELECT COUNT(*) FROM salaries) / 2
        """
    )
    result = cursor.fetchall()
    print(result)  # медианная зарплата - 10085
    # endregion

    # region subtask_4
    cursor.execute(
        """
            SELECT 100 * ROUND(X / Y, 2);
            X = SELECT SUM(salary) FROM TOP10;
            TOP10 = SELECT SUM(salary) FROM salaries ORDER BY salary DESC LIMIT 0.1 * TOTAL;
            TOTAL = SELECT COUNT(salary) FROM salaries;
        """
    )
    result = cursor.fetchall()
    print(result)  # медианная зарплата - 10085
    # endregion
