import re
import textwrap

from . import exceptions


class Translator:
    # https://ru.wikipedia.org/wiki/Римские_цифры#Регулярные_выражения
    ROMAN_REGEX = re.compile(
        '^(M{0,3})(D?C{0,3}|C[DM])(L?X{0,3}|X[LC])(V?I{0,3}|I[VX])$'
    )

    # https://ru.wikipedia.org/wiki/Римские_цифры#Римские_цифры
    __ADDITION_RULES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    __SUBTRACTION_RULES = {
        'IV': 2,
        'IX': 2,
        'XL': 20,
        'XC': 20,
        'CD': 200,
        'CM': 200,
    }

    @staticmethod
    def translate_to_arabic(roman_numerals: str) -> int:
        Translator.__ensure_is_roman(roman_numerals)

        result = 0
        for chunk in Translator.__chunked(roman_numerals):
            for symbol in chunk:
                result += Translator.__ADDITION_RULES[symbol]
            result -= Translator.__SUBTRACTION_RULES.get(chunk, 0)

        return result

    @staticmethod
    def is_roman(numerals: str) -> bool:
        return bool(Translator.ROMAN_REGEX.match(numerals))

    @staticmethod
    def __ensure_is_roman(numerals: str) -> None:
        if not Translator.is_roman(numerals):
            message = f'Numerals should match pattern {Translator.ROMAN_REGEX.pattern}'
            raise exceptions.NumeralsAreNotRomansError(message)

    @staticmethod
    def __chunked(string: str) -> 'list[str]':
        return textwrap.wrap(string, 2)
