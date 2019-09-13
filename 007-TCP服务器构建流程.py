# 导入 socket 模块
from socket import *

# 创建服务器套接字
server_socket = socket(AF_INET, SOCK_STREAM)

# 服务器套接字绑定ip和port
server_ip = ""
server_port = 8080
server_socket.bind((server_ip, server_port))

# 将服务器套接字变为被动套接字
server_socket.listen(128)

# 等到客户端的链接
client_socket, client_addr = server_socket.accept()
print("client_socket:%s" % str(client_socket))
print("client_addr:%s" % str(client_addr))

# 接受数据
recv_data = client_socket.recv(1024)
print("接收到的数据：", recv_data.decode("utf-8"))

# 发送数据
send_data = "服务器给你的数据"
client_socket.send(send_data.encode("utf_8"))

# 关闭套接字
client_socket.close()
server_socket.close()
