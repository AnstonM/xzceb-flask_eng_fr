import unittest

from translator import french_to_english, english_to_french

class TestF2E(unittest.TestCase):
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english(" ")," ")
        self.assertEqual(french_to_english('Pain'),'Bread')
        self.assertEqual(french_to_english('Boire'),'Drink')

class TestE2F(unittest.TestCase):
    def test2(self): 
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french(' '),' ')
        self.assertEqual(english_to_french('Woman'),'Femme')
        self.assertEqual(english_to_french('Man'),'Homme')

unittest.main()