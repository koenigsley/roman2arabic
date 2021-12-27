from roman2arabic.translator import Translator

from roman2arabic import exceptions


def translate(roman_numerals: str) -> None:
    try:
        arabic_numbers = Translator.translate_to_arabic(roman_numerals)
        print(arabic_numbers)
    except exceptions.TranslatorError as ex:
        print(str(ex))
