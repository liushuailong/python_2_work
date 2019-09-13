# 导入 socket 模块
from socket import *

#创建客户端套接字
tcp_socket = socket(AF_INET, SOCK_STREAM)

#链接服务器
server_ip = "192.168.0.103"
server_port = 8080
tcp_socket.connect((server_ip, server_port))

#向服务器发送请求
send_data = input("请输入要发送的数据：")
tcp_socket.send(send_data.encode("utf-8"))

#接受服务器发回的数据
recv_data = tcp_socket.recv(1024)
print("接受到的数据为：", recv_data.decode("utf-8"))

#关闭套接字
tcp_socket.close()
