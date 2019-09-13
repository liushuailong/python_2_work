# 导入 socket 模块
from socket import *

# 创建服务器端套接字
udp_server_socket = socket(AF_INET, SOCK_DGRAM)

# 绑定本地的相关信息，如果一个网络程序不绑定，则系统随机分配
local_addr = ("", 8080)
udp_server_socket.bind(local_addr)

# 等待接受对方发送的数据
recv_data = udp_server_socket.recvfrom(1024)

# 显示接受到的数据
print(recv_data[0].decode("utf-8"))

# 关闭套接字
udp_server_socket.close()

