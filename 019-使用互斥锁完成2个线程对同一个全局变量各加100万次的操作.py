import threading
import time


g_num = 0


def work1(num, mutex):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("__in work1: g_num is {}".format(g_num))


def work2(num, mutex):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1 
        mutex.release()
    print("__in work2: g_num is {}".format(g_num))


def main():
    mutex = threading.Lock()
    # num = 100 or 10000000
    num = 10000000
    t1 = threading.Thread(target=work1, args=(num, mutex))
    t1.start()
    t2 = threading.Thread(target=work2, args=(num, mutex))
    t2.start()

    while len(threading.enumerate()) != 1:
        time.sleep(1)
        
    
    
if __name__ == "__main__":
    main()
    
