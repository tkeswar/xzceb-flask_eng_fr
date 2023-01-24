import unittest

from translator import english_to_french, french_to_english

class TestenglishToFrench(unittest.TestCase): 
    def test1(self):
        self.assertEqual(english_to_french(''),'') #test for null string
    def test2(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour') #test for Hello to Bonjour translation


class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self):
        self.assertEqual(french_to_english(''),'') #test for null string
    def test2(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello') #test for Bonjour to Hello translation



unittest.main()

