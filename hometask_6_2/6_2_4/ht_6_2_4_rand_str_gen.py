import random
import string
import sys
import os

'''Script generate random strings. Need take 2 command line arguments. First - file_name for result file. Second - count strings to generate'''

file_name = sys.argv[1]
string_num = sys.argv[2]

def gen_rand_str():
    return ''.join([random.choice(string.ascii_letters + ' ') for i in range(2, random.randrange(2, 101))])
    
with open(f'{os.getcwd()}\\{file_name}', 'a') as f:
    for i in range (int(string_num)):
        f.writelines(f'{gen_rand_str()}\n')