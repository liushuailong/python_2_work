# 导入 threading 模块
import threading
# 导入 time 模块实现延时功能
import time

g_nums = [11, 22, 33]

def work1(nums):
    nums.append(44)
    print("___in work1:{}".format(nums))    


def work2(nums):
    time.sleep(1)
    print("___in work2:{}".format(nums))


def main():
    # 创建一个线程,去修改g_num的值
    t1 = threading.Thread(target=work1, args=(g_nums,))
    # 启动线程1
    t1.start()
    # 设置延时，讲线程1运行完毕
    time.sleep(1)
    # 创建另一个线程打印个g_num的值
    t2 = threading.Thread(target=work2, args=(g_nums,))
    t2.start()


if __name__ == "__main__":
    main()
