import argparse
from is_valid import is_valid

'''Func check brackets validation from lines in file_for_validation as command line arg'''

parser = argparse.ArgumentParser(description='Check brackets validation. Enter filename for validate as first arg')
parser.add_argument("file_for_validation", type=str, help="Filename for validation")
args = parser.parse_args()

with open(args.file_for_validation) as f:
    if not is_valid(f.read()): print('Error! Brackets invalid!')