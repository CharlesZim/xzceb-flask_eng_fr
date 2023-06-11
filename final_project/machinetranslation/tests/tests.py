import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hi"), "Bonjour")
        self.assertNotEqual(english_to_french("Hi"), "Au revoir")

    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Au revoir"), "Hi")

if __name__ == '__main__':
    unittest.main()

