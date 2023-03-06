import unittest
from urfu_python_advanced.module3.task4.main import Person


class TestPerson(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.person = Person(
            name="Tom", year_of_birth=2003, address="Somewhere")

    def test_get_correct_age(self):
        self.assertEqual(self.person.get_age(), 20)

    def test_get_name(self):
        self.assertEqual(self.person.name, self.person.get_name())

    def test_set_name(self):
        self.person.set_name("Dan")
        self.assertEqual(self.person.get_name(), "Dan")

    def test_get_address(self):
        self.assertEqual(self.person.address, self.person.get_address())

    def test_set_address(self):
        self.person.set_address("Nowhere")
        self.assertEqual(self.person.get_address(), "Nowhere")

    def test_is_homeless(self):
        self.person.set_address(None)
        self.assertTrue(self.person.is_homeless())
