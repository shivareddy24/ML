import multiprocessing
import sys
import time
import math

sys.set_int_max_str_digits(100000)

def factorial(num):
    print(f"Calculating factorial of {num}...")
    result = math.factorial(num)
    print(f"Number of digits in factorial of {num} is {len(str(result))}")
    return result

if __name__ == '__main__':
    numbers = [1234, 4566, 876, 5000]
    start_time = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(factorial, numbers)

    endtime = time.time() - start_time
    print(f"Executed in {endtime:.2f} sec")
