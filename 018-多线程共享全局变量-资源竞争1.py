import threading
import time


g_num = 0


def work1(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("__in work1: g_num is {}".format(g_num))


def work2(num):
    global g_num
    for i in range(num):
        g_num += 1 
    print("__in work2: g_num is {}".format(g_num))


def main():
    print("__线程创建之前g_num is {}".format(g_num))
    # num = 100 or 10000000
    num = 10000000000
    t1 = threading.Thread(target=work1, args=(num,))
    t1.start()
    t2 = threading.Thread(target=work2, args=(num,))
    t2.start()

    while len(threading.enumerate()) != 1:
        time.sleep(1)
        
    print("2个线程对同一个全局变量操作之后的最终结果是：{}".format(g_num))
    
    
if __name__ == "__main__":
    main()
    
