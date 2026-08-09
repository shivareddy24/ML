import multiprocessing
import time

def print_nums():
    for i in range(10):
        time.sleep(1)
        print(f"number is {i}")

def print_letters():
    for letter in "shivareddy":
        time.sleep(1)
        print(f"letter is {letter}")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=print_nums)
    p2 = multiprocessing.Process(target=print_letters)

    curr_time = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    final_time = time.time() - curr_time
    print(f"execution completed by taking time {final_time:.2f} seconds")
