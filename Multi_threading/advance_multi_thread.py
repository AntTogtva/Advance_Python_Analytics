# multithreading with thread pool executor 

from concurrent.futures import ThreadPoolExecutor

import time 

def print_number(number):
    time.sleep(1)
    return (f' number: {number}')

numbers=[num for num in range(5)]

with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(print_number,numbers)

for result in results:
    print(result)