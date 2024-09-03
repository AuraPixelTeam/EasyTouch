import argparse
from commands import *


def main():
    parser = argparse.ArgumentParser(description='Manage files and folders more easily')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    touch_parser = subparsers.add_parser('touch', help='Create a new file with the specified name')
    touch_parser.add_argument('filename', type=str, help='The name of the file to create')

    mv_parser = subparsers.add_parser('mv', help='Move or rename a file')
    mv_parser.add_argument('source', type=str, help='The source file to move or rename')
    mv_parser.add_argument('destination', type=str, help='The destination path or new filename')

    rm_parser = subparsers.add_parser('rm', help='Remove (delete) a file or directory')
    rm_parser.add_argument('filename', type=str, help='The file or directory to delete')
    rm_parser.add_argument('-r', '--recursive', action='store_true',
                           help='Recursively delete a directory and its contents')

    args = parser.parse_args()

    if args.command == 'touch':
        touch_file(args.filename)
    elif args.command == 'mv':
        move_file(args.source, args.destination)
    elif args.command == 'rm':
        remove_file(args.filename, args.recursive)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
