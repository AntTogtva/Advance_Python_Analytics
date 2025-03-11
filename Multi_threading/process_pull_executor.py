# mutiprocessing by process pull executor 
from concurrent.futures import ProcessPoolExecutor

import time 

def square_number(number):
    time.sleep(1)
    return f"square : {number*number}"

numbers=[num for num in range(5)]

if __name__ =='__main__':
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number,numbers)

    for result in results:
        print(result)