import random
import sqlite3
import time

import requests
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool

url = "https://swapi.dev/api/people/"
sql_request = "insert into people (name, birth_year, gender) VALUES (?,?,?)"
people = []


def get_random_person(*args):
    response = requests.get(url + str(random.randint(1, 82)))
    if response.status_code == 200:
        person = dict(response.json())
        return person["name"], person["birth_year"], person["gender"]


def download_people_pool(cursor: sqlite3.Cursor):
    start = time.time()
    with Pool(processes=20) as pool:
        people = list(pool.map(get_random_person, [i for i in range(20)]))
    print(f"Time taken: {(time.time() - start):0.4f}s")
    cursor.executemany(sql_request, people)


def download_people_threadpool(cursor: sqlite3.Cursor):
    start = time.time()
    with ThreadPool(processes=20) as pool:
        people = list(pool.map(get_random_person, [i for i in range(20)]))
    print(f"Time taken: {(time.time() - start):0.4f}s")
    cursor.executemany(sql_request, people)


if __name__ == "__main__":
    with sqlite3.connect("urfu_python_advanced/module12/task.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "create table if not exists people (name string, birth_year string, gender string)"
        )
        cursor.execute("delete from people")

        # download_people_pool(cursor)  # Time taken: 16.7087s
        download_people_threadpool(cursor)  # Time taken: 15.6656s
