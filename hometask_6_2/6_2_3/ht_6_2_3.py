import argparse
import os
from is_valid import is_valid

'''Func validate brackets in file or dir, that pointed in commandline arg'''

parser = argparse.ArgumentParser(description='Validate brackets validation. Enter filename or dir for validate as first arg')
parser.add_argument("target_pointer", type=str, help="place (dir or file) for validation")
args = parser.parse_args()
#args =  Namespace(target_pointer='.\\slrm_py_bcknd\\hometask_6_2\\6_2_3\\dir_asserts\\assert_2.txt')
if os.path.isdir(args.target_pointer):
    for i in os.listdir(args.target_pointer):
        if i.endswith('.txt'):
            with open(f'{args.target_pointer}{i}') as f:
                if not is_valid(f.read()): print(f'{i}: Error! Brackets invalid!')
                else: print(f'{i}: Valid!')
else:
    with open(args.target_pointer) as f:
        if not is_valid(f.read()): print('Error! Brackets invalid!')