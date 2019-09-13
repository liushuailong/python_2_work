# -*- coding:utf-8 -*-
import time
import threading


def saySorry():
    print("亲爱的，我能吃饭吗？")
    
    
if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=saySorry)
        t.start() # 启动线程，既让线程开始执行
