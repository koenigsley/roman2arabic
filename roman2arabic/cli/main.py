from argparse import ArgumentParser

from . import commands


def main() -> None:
    parser = ArgumentParser(
        prog='roman2arabic',
        description='Roman numerals translator',
    )

    subparsers = parser.add_subparsers(dest='command')

    translate = subparsers.add_parser('translate',
                                      help='Translates Roman numerals to Arabic numbers')
    translate.add_argument('-r', '--roman', type=str, dest='roman')

    args = parser.parse_args()

    if args.command == 'translate':
        commands.translate(args.roman)
    else:
        parser.print_help()
