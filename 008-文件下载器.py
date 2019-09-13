# -*- coding:utf-8 -*-

 # 导入 socket 模块
from socket import *
import sys


def send_file(file_name):
    # 判断文件是否存在
    try:
        with open(file_name, "rb") as f:
            content = f.read()
        return content
    except:
        print("没有下载的文件:{}".format(file_name))


def main():
    # 从终端获取端口
    # 判断用户是否正确输入端口好
    if len(sys.argv) != 2:
        print("请按照如下方式运行：python3 fileName.py port")
        return
    else:
        if 1024 < int(sys.argv[1]) < 65535:
            port = int(sys.argv[1])
        else:
            print("请输入正确的端口号")
            return 
    # 创建套接字
    server_socket = socket(AF_INET, SOCK_STREAM)
    # 套接字绑定ip和port
    # server_socket.bind(("", 8080))
    server_socket.bind(("", port))
    # 将套接字变为被动套接字
    server_socket.listen(128)
    # 接受客户端的链接
    while True:
        client_socket, client_addr = server_socket.accept()
        # 接受客户端的请求数据
        recv_data = client_socket.recv(1024)
        file_name = recv_data.decode("utf-8")
        # print("文件名：", file_name)
        # 发送数据给客户端
        file_data = send_file(file_name)
        if file_data:
            client_socket.send(file_data)
        client_socket.close()
    server_socket.close()
    

if __name__ == "__main__":
    main()
