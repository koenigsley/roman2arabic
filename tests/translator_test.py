import unittest

from roman2arabic.translator import Translator


class MyTestCase(unittest.TestCase):
    def test_should_translate_MMIX_2009(self):
        self.assertEqual(2009, Translator.translate_to_arabic('MMIX'))

    def test_should_translate_XLIII_to_43(self):
        self.assertEqual(43, Translator.translate_to_arabic('XLIII'))

    def test_should_translate_XC_to_90(self):
        self.assertEqual(90, Translator.translate_to_arabic('XC'))

    def test_should_translate_CD_to_400(self):
        self.assertEqual(400, Translator.translate_to_arabic('CD'))

    def test_should_translate_CMXCVII_to_997(self):
        self.assertEqual(997, Translator.translate_to_arabic('CMXCVII'))
