# python 中使用socket模块中的函数 socket 就可以完成socket的创建
# import socket
# socket.socket(AddressFamily, Type)

# 创建一个 TCP 套接字
# 导入socket模块
import socket

# 创建套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 这里使用套接字的功能:收发数据

# 不用的时候，关闭套接字
s.close()


# 创建一个 UDP 套接字
# 导入 socket 模块
import socket

# 创建套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 这里使用套接字的功能:收发数据

# 不用的时候，关闭套接字
s.close()

