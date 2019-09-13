# -*- coding:utf-8 -*-
from multiprocessing import Process
import os
from time import sleep


def run_proc(name, age, **kwargs):
    for i in range(10):
        print("子进程运行中，name={},age={},pid={}".format(name, age, os.getpid()))
        print(kwargs)
        sleep(0.2)
        

if __name__ == "__main__":
    p = Process(target=run_proc, args=("test", 18), kwargs={"m":20})
    p.start()
    sleep(1)
    p.terminate() # 1 秒钟后立即结束子进程
    p.join()
