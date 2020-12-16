
import threading
import time


shared_number = 0
lock = threading.Lock()

def thread_1(number):
    global shared_number
    lock.acquire()
    print("number = ",end=""), print(number)
    for i in range(number):
        shared_number += 1
    lock.release()

def thread_2(number):
    global shared_number
    lock.acquire()
    print("number = ",end=""), print(number)
    for i in range(number):
        shared_number += 1
    lock.release()

if __name__ == "__main__":

    threads = [ ]

    start_time = time.time()
    t1 = threading.Thread( target= thread_1, args=(50000000,) )
    t1.start()
    threads.append(t1)

    t2 = threading.Thread( target= thread_2, args=(50000000,) )
    t2.start()
    threads.append(t2)

    for t in threads:
        t.join()

    print("--- %s seconds ---" % (time.time() - start_time))

    print("shared_number=",end=""), print(shared_number)
    print("end of main")
