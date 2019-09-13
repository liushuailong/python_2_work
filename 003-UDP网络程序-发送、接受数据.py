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
dest_addr = input("192.168.0.103", 8080)

    # 从键盘获取数据
send_data = input("请输入要发送的数据：")

# 发送数据到制定电脑上的指定程序中
udp_socket.sendto(send_data.encode("utf-8"), dest_addr)

# 等待接收对方发送的数据
recv_data = udp_socket.recvfrom(1024)

# 显示对方发送的数据
# print(recv_data)
# ----> (b'\xe5\x88\x98\xe5\xb8\x85\xe9\xbe\x99\xef\xbc\x8c\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x81', ('192.168.0.103', 8080))
# 使用recvfrom收到的数据是一个元组，含有两个元素,第一个元素是对方发送的信息（二进制编码）的字符串，第二个元素是一个含有两个元素的元组，表示对方的IP(字符串）和端口号信息(一个整数）
print(recv_data[0].decode("utf-8")

# 关闭套接字
udp_socket.close()

