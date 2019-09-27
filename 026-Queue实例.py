# -*- coding:utf-8 -*-

"""
在父进程中创建连个子进程，一个往进程中写数据，一个从Queue里读取数据
"""

# 导入用到的模块
from multiprocessing import Process, Queue
import os, time, random


def write_queue(q):
    for value in ["A", "B", "C", "D"]:
        print('put {} to queue...'.format(value))
        q.put(value)
        time.sleep(random.random())


def read_queue(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print("Get {} from queue...".format(value))
            time.sleep(random.random())
        else:
            break


if __name__ == "__main__":
    # 实例化一个队列
    q = Queue(5)
    # 在父进程中创建连个子进程
        # 在一个子进程中向队列中写如消息
    p1 = Process(target=write_queue, args=(q,))
        # 在另一个子进程中读取队列中的消息
    p2 = Process(target=read_queue, args=(q,))
    
    #开启子进程
    p1.start()
    p1.join()
    p2.start()
    p2.join()

    print('')
    print("over")



