from roman2arabic.translator import Translator


def translate(roman_numerals: str) -> None:
    try:
        arabic_numbers = Translator.translate_to_arabic(roman_numerals)
        print(arabic_numbers)
    except Translator.TranslatorError as ex:
        print(str(ex))
