import threading
import time

def print_nums():
    for i in range(10):
        time.sleep(1)
        print(f"number is {i}")
def print_letters():
    for letter in "shivareddy":
        time.sleep(1)
        print(f"number is {letter}")

t1=threading.Thread(target=print_nums)
t2=threading.Thread(target=print_letters)

curr_time=time.time()
t1.start()
t2.start()

t1.join()
t2.join()

final_time = time.time() - curr_time
print(f"execution completed by taking time {final_time}")
    