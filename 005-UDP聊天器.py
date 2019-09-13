"""
在一个电脑中编写1个程序，有2个功能
1.获取键盘数据，并将其发送给对方
2.接收数据并显示
并且功能数据进行选择以上的2个功能调用
"""
# 导入 socket 模块
from socket import *

def menu():
    print("请您选择以下功能：")
    print("1. 发送数据")
    print("2. 接受数据")
    print("3. 退出程序")


def send_data(client_socket):
    # print("发送数据")
    send_datas = input("请输入要发送的数据: ")
    desc_addr = ("192.168.0.105", 8080)
    client_socket.sendto(send_datas.encode("utf-8"), desc_addr)
    
    
def recv_data(client_socket):
    # print("接受数据")
    recv_data = client_socket.recvfrom(1024)
    print("="*10)
    print("来自%s:%d的信息" % recv_data[1])
    print(recv_data[0].decode("utf-8"))
    print("="*10)


def main():
    # 创建套接字

    client_socket = socket(AF_INET, SOCK_DGRAM)
    src_addr = ("", 8080)
    client_socket.bind(src_addr)

    #功能菜单
    while True:
        menu()
        order_data = input("请选择功能：")
        if order_data == "1":
            # 功能1：发送数据
            send_data(client_socket)
        elif order_data == "2":
            # 功能2: 接受数据病显示
            recv_data(client_socket)
        elif order_data == "3":
            break
        else:
            print("您选择的功能不存在")


if __name__ == "__main__":
    main()
