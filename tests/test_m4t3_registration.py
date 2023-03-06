import unittest
from urfu_python_advanced.module4.main import app


class TestRegistration(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.base_url = "/registration"
        self.correct_payload = {
            "email": "test@google.com",
            "phone": 9999999990,
            "name": "Tom",
            "address": "Russia",
            "index": 123,
            "comment": "Comment"
        }

    def test_can_use_valid_email(self):
        payload = {"email": "test@google.com"}
        response = self.app.post(
            self.base_url, data=self.correct_payload | payload)
        self.assertEqual(response.status_code, 200)

    def test_can_use_valid_phone(self):
        payload = {"phone": 9999999998}
        response = self.app.post(
            self.base_url, data=self.correct_payload | payload)
        self.assertEqual(response.status_code, 200)

    def test_can_use_valid_name(self):
        payload = {"name": "Dan"}
        response = self.app.post(
            self.base_url, data=self.correct_payload | payload)
        self.assertEqual(response.status_code, 200)

    def test_can_use_valid_address(self):
        payload = {"address": "USA"}
        response = self.app.post(
            self.base_url, data=self.correct_payload | payload)
        self.assertEqual(response.status_code, 200)

    def test_can_use_valid_index(self):
        payload = {"index": 321}
        response = self.app.post(
            self.base_url, data=self.correct_payload | payload)
        self.assertEqual(response.status_code, 200)

    def test_can_use_valid_comment(self):
        payload = {"comment": "Another comment"}
        response = self.app.post(
            self.base_url, data=self.correct_payload | payload)
        self.assertEqual(response.status_code, 200)

    def test_invalid_email_raises_error(self):
        payload = {"email": "test"}

        response = self.app.post(
            self.base_url, data=self.correct_payload | payload)
        self.assertEqual(response.status_code, 400)

    def test_invalid_phone_raises_error(self):
        payload = {"phone": "test"}

        response = self.app.post(
            self.base_url, data=self.correct_payload | payload)
        self.assertEqual(response.status_code, 400)

    def test_invalid_name_raises_error(self):
        payload = {"name": None}

        response = self.app.post(
            self.base_url, data=self.correct_payload | payload)
        self.assertEqual(response.status_code, 400)

    def test_invalid_address_raises_error(self):
        payload = {"address": None}

        response = self.app.post(
            self.base_url, data=self.correct_payload | payload)
        self.assertEqual(response.status_code, 400)

    def test_invalid_index_raises_error(self):
        payload = {"index": "test"}

        response = self.app.post(
            self.base_url, data=self.correct_payload | payload)
        self.assertEqual(response.status_code, 400)
