from roman2arabic.translator import Translator
from .handlers import catch_translator_error


@catch_translator_error
def translate(roman_numerals: str) -> None:
    arabic_number = Translator.translate_to_arabic(roman_numerals)
    print(arabic_number)
