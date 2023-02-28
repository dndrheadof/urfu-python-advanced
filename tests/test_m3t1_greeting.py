import unittest
from freezegun import freeze_time
from urfu_python_advanced.module3.task1.main import app


class TestGreetingApp(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.app = app.test_client()
        self.base_url = "/hello-world/"

    def test_can_get_correct_greeting(self):
        username = "Игорь"
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    @freeze_time("2023-02-27")
    def test_can_get_correct_greeting_and_weekday(self):
        username = "Игорь"
        greeting = "Хорошего понедельника!"
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(greeting in response_text)
