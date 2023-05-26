import random
import sqlite3
import time

import requests
import concurrent.futures

url = "https://swapi.dev/api/people/"
sql_request = "insert into people (name, birth_year, gender) VALUES (?,?,?)"
people = []


def get_random_person():
    response = requests.get(url + str(random.randint(1, 82)))
    if response.status_code == 200:
        person = dict(response.json())
        people.append((person["name"], person["birth_year"], person["gender"]))


def download_people(cursor: sqlite3.Cursor):
    start = time.time()
    [get_random_person() for _ in range(20)]

    cursor.executemany(sql_request, people)
    print(f"Time taken: {(time.time() - start):0.4f}s")


def download_people_multithread(cursor: sqlite3.Cursor):
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        res = [executor.submit(get_random_person)] * 20
        concurrent.futures.wait(res)

        cursor.executemany(sql_request, people)
    print(f"Time taken: {(time.time() - start):0.4f}s")


if __name__ == "__main__":
    with sqlite3.connect("urfu_python_advanced/module11/task.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "create table if not exists people (name string, birth_year string, gender string)"
        )
        cursor.execute("delete from people")

        # download_people(cursor)  # Time taken: 8.7099s
        download_people_multithread(cursor)  # Time taken: 1.2919s
