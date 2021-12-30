from functools import wraps

from roman2arabic.exceptions import TranslatorError


def catch_translator_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TranslatorError as err:
            print(err)
    return wrapper
