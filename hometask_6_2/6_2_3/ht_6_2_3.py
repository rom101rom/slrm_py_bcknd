import os
import argparse
from is_valid import is_valid

'''Func validate brackets in file or recursive dir, that pointed in commandline arg'''
parser = argparse.ArgumentParser(description='Validate brackets validation. Enter filename or dir for validate as first arg')
parser.add_argument("target_pointer", type=str, help="place (dir or file) for validation")
args = parser.parse_args()

if os.path.isdir(args.target_pointer):
    for root, dirs, files in os.walk(args.target_pointer):
        for file in files:
            if file.endswith('.txt'):
                with open(f'{root}/\\{file}') as f:
                    if not is_valid(f.read()):
                        with open(f'{args.target_pointer}\\solution.txt', 'a') as m:
                            m.write(f'{file} Error! Brackets invalid!\n')
                    else:
                        with open(f'{args.target_pointer}\\solution.txt', 'a') as m:
                            m.write(f'{file} Valid!\n')
else:
    with open(args.target_pointer) as f:
        if not is_valid(f.read()):
           with open(f'{os.getcwd()}\\solution.txt', 'a') as m:
                            m.write(f'{f.name[2::]} Error! Brackets invalid!\n')
        else:
             with open(f'{os.getcwd()}\\solution.txt', 'a') as m:
                            m.write(f'{f.name[2::]} Valid!\n')