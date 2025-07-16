from platform import system
from string import ascii_uppercase
from pathlib import Path
from argparse import (ArgumentParser)

drive_format = '{drive}:\\'
to_scan = [
    Path(drive_format.format(drive=drive)).absolute() for drive in ascii_uppercase if Path(drive_format.format(drive=drive)).exists()
] if system() == 'Windows' else [Path('/')]

parser = ArgumentParser()
parser.add_argument('-f', '--f', action='store_true', help='Search by file name')
parser.add_argument('-d', '--d', action='store_true', help='Search by directory name')
parser.add_argument('-e', '--e', action='store_true', help='Search files by extension')
args = parser.parse_args()
if args.f:
    file_to_search = input('file> ').lower()

if args.d:
    directory_to_search = input('directory> ').lower()

if args.e:
    extension_to_search = input('extension> ').lower()

for drive in to_scan:
    try:
        for root, directories, files in Path(drive).walk():
            if args.f:
                for file in files:
                    file = Path(root, file)
                    if (file.name.lower() == file_to_search):
                        print(file)

            if args.d:
                for directory in directories:
                    directory = Path(root, directory)
                    if (directory.name.lower() == directory_to_search):
                        print(directory)

            if args.e:
                for file in files:
                    file = Path(root, file)
                    if (file.suffix.lower() == extension_to_search):
                        print(file)

    except PermissionError:
        pass
