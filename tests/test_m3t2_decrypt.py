import unittest
from urfu_python_advanced.module3.task2.main import decrypt


class TestDecrypt(unittest.TestCase):
    def test_decrypt(self):
        self.assertEqual(decrypt("абра-кадабра."), "абра-кадабра")
        self.assertEqual(decrypt("абраа..-кадабра"), "абра-кадабра")
        self.assertEqual(decrypt("абраа..-.кадабра"), "абра-кадабра")
        self.assertEqual(decrypt("абра--..кадабра"), "абра-кадабра")
        self.assertEqual(decrypt("абрау...-кадабра"), "абра-кадабра")
        self.assertEqual(decrypt("абра........"), "")
        self.assertEqual(decrypt("абр......а."), "а")
        self.assertEqual(decrypt("1..2.3"), "23")
        self.assertEqual(decrypt("."), "")
        self.assertEqual(decrypt("1......................."), "")
        self.assertEqual(decrypt("te...st.."), "ts")
