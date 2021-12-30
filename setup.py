from setuptools import setup, find_packages

setup(
    name='roman2arabic',
    version='0.1.0',
    description='Python package designed to convert Roman numerals to Arabic numbers',
    author='Mikhail Eremeev',
    author_email='meremeev@sfedu.ru',
    url='https://github.com/tediore-wf/roman2arabic',
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.8',
    entry_points={
        'console_scripts': ['roman2arabic=roman2arabic.cli.main:main'],
    },
    platforms=['any'],
)
