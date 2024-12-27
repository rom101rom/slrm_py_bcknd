import sys
import os
import random
import string
import asyncio
import datetime
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

loop = asyncio.get_event_loop()
executor = ProcessPoolExecutor(max_workers=multiprocessing.cpu_count())


def gen_rand_str(lines_num) -> list:    #task (worker)
    res = []
    for i in range(int(lines_num)):
        res.append(''.join([random.choice(string.ascii_letters + ' ') for i in range(2, random.randrange(2, 101))]))
    return res

async def create_coro(num: int):
    return await loop.run_in_executor(executor, gen_rand_str, num)


def main():
    file_name = sys.argv[1]
    string_num = int(sys.argv[2])

    with open(f'{os.getcwd()}\\{file_name}', 'a') as f:
        tasks = [
           asyncio.ensure_future(create_coro(string_num // multiprocessing.cpu_count()))
           for _ in range(multiprocessing.cpu_count())
       ]
        for l in loop.run_until_complete(asyncio.gather(*tasks)):
           for s in l:
               f.write(f'{s}\n')



if __name__ == "__main__":
   start = datetime.datetime.now()
   main()
   finish = datetime.datetime.now()
   print(f'Total time for execute: {finish - start}')