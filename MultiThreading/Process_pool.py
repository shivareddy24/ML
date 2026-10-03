from concurrent.futures import ProcessPoolExecutor
import time

def squares(nums):
    time.sleep(2)
    return nums**2

if __name__=="__main__":
    start_time = time.time()
    numbers = [1,2,3,4,5,6,7,8,9]

    with ProcessPoolExecutor(max_workers=3) as execution :
        results = execution.map(squares,numbers)

    for result in results:
        print(result)

    finish_time = time.time() - start_time
    print(f"code finished in {finish_time}")