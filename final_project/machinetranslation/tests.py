#Write at least 2 tests in tests.py for each method
import unittest
from translator import *

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        #Test for null input for englishToFrench.
        self.assertEqual(frenchText, '')
        #Test for the translation of the world 'Hello' and 'Bonjour'.
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

    def test_frenchToEnglish(self):
        #Test for null input for frenchToEnglish
        self.assertEqual(englishText, '')
        #Test for the translation of the world 'Bonjour' and 'Hello'.
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

if __name__=='__main__':
        unittest.main()
