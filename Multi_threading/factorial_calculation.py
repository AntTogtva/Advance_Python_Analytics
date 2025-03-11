import sys 
import multiprocessing
import math
import time 

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

# Function to compute the factorial of a given number
def computer_factorial(number):
    print(f'factorial of : {number}')
    result = math.factorial(number)
    print(f'factorial of {number} is {result}')
    return result

if __name__ == '__main__':
    numbers = [5000, 600, 7000, 8000]
    start_time = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(computer_factorial, numbers)

    end_time = time.time() - start_time

    print(f'results: {results}')
    print(f'time taken: {end_time} seconds')
