# 导入 threading 模块
import threading
# 导入 time 模块实现延时功能
import time

g_num = 100

def work1():
    global g_num
    for i in range(3):
        g_num +=1
    print("___in work1:{}".format(g_num))    


def work2():
    global g_num
    print("___in work2:{}".format(g_num))


def main():
    # 创建一个线程,去修改g_num的值
    t1 = threading.Thread(target=work1)
    # 启动线程1
    t1.start()
    # 设置延时，讲线程1运行完毕
    time.sleep(1)
    # 创建另一个线程打印个g_num的值
    t2 = threading.Thread(target=work2)
    t2.start()


if __name__ == "__main__":
    main()
