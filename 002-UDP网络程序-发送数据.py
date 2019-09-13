"""
创建一个基于udp的网络程序流程：
1. 创建客户端套接字
2. 发送、接受数据
3. 关闭套接字
"""

# 导入 socket 模块
from socket import *

# 创建客户端套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 发送数据
    # 准备接收方的地址
dest_addr = ("192.168.0.103", 8080)

    # 从键盘获取数据
send_data = ("请输入要发送的数据：")

# 发送数据到制定电脑上的指定程序中
udp_socket.sendto(send_data.encode("utf-8"), dest_addr)

# 关闭套接字
udp_socket.close()

