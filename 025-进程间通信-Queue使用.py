# -*- coding:utf-8 -*-


# 导入模块
from multiprocessing import Queue
"""
q = Queue(n) : 创建能存放n个消息的队列
q.put("element") : 向队列中添加元素
q.get("element") : 从队列中取出元素
q.put_nowait() / q.get_nowait() : 存放或读取消息时不等待立马执行,条件不满足立马抛出异常
q.full() : 判断队列是否已满
q.empty() : 判断队列是否为空 
q.qsize() : 返回当钱队列包含的消息的数量
"""


# 创建队列
q = Queue(3)
# 向队列中放入数据
q.put("note 1")
q.put("note 2")
# 判断队列是否已满
print(q.full())
q.put("note 3")
print (q.full())

# 因为消息队列已满的情况下会抛出异常，第一个try会等待2秒后在抛出异常，第二个try会立即抛出异常
try:
    q.put("note 4", True, 2)
except:
    print("note queue is full, the num of queue is:{}".format(q.qsize()))


try:
    q.put_nowait("note 4")
except:
    print("note is full, the num of queue is:{}".format(q.qsize()))


# 推荐的方式，先判断消息队列是否已满，再写入
if not q.full():
    q.put_nowait("note 4")
    

# 读取消息时，先判断消息队列是否为空，再读取
if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())

