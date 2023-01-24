import unittest

from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase): 
    def test1(self):
        self.assertEqual(englishToFrench(None),None) #test for null string
    def test2(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour') #test for Hello to Bonjour translation


class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self):
        self.assertEqual(frenchToEnglish(None),None) #test for null string
    def test2(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello') #test for Bonjour to Hello translation



unittest.main()

