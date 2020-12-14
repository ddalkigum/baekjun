
from multiprocessing import Process, Queue, Value
import time

def worker(id, number, q):
    increased_number = 0

    for i in range(number):
        increased_number += 1
    
    print(q)
    print(dir(q))

    return

if __name__ == "__main__":

    start_time = time.time()
    q = Value("i",0)

    th1 = Process(target=worker, args=(1, 50000000, q))
    th2 = Process(target=worker, args=(2, 50000000, q))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print("--- %s seconds ---" % (time.time() - start_time))
    q.put('exit')

    total = 0
    while True:
        tmp = q.get()
        if tmp == 'exit':
            break
        else:
            total += tmp

    print("total_number=",end=""), print(total)
    print("end of main")
