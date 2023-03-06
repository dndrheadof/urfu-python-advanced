import unittest
from urfu_python_advanced.module3.task3.main import *
import json


class TestExpenses(unittest.TestCase):
    @classmethod
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.app = app.test_client()
        self.add_url = "/add"
        self.calculate_url = "/calculate"
        self.expenses = {
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

    def test_add_raises_error(self):
        date = "123"
        expense = 100

        with self.assertRaises(ValueError):
            self.app.get(f"{self.add_url}/{date}/{expense}")

    def test_can_get_correct_expenses(self):
        date = "20230101"
        expense = 100
        response = self.app.get(f"{self.add_url}/{date}/{expense}")
        response_data = response.data.decode()

        self.assertDictEqual(json.loads(response_data), {
            "2022": {
                "12": {
                    "31": 123,
                    "12": 100
                },
                "11": {
                    "12": 122,
                    "14": 1331
                }
            },
            "2023": {
                "2": {
                    "27": 1279
                },
                "1": {
                    "1": 100
                }
            }
        })

    def test_calculate_expenses(self):
        year = 2022
        result = "1676"
        response = self.app.get(f"{self.calculate_url}/{year}")
        response_data = response.data.decode()

        self.assertTrue(result in response_data)

    def test_add_and_calculate_expenses(self):
        date = 20221212
        expense = 100
        year = 2022
        result = "1676"
        response = self.app.get(f"{self.add_url}/{date}/{expense}")
        response = self.app.get(f"{self.calculate_url}/{year}")
        response_data = response.data.decode()

        self.assertTrue(result in response_data)
