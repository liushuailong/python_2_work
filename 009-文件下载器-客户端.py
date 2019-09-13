from socket import *


def save_data(recv_data, file_name):
    with open(file_name, "wb") as f:
        f.write(recv_data)


def main():
    # 创建客户端套接字
    client_socket = socket(AF_INET, SOCK_STREAM)
    # 链接服务器
    client_socket.connect(("192.168.0.103", 8080))
    # 向服务器请求数据
    file_name = input("请输入你想下载的文件名：")
    client_socket.send(file_name.encode("utf-8"))
    
    recv_data = client_socket.recv(1024)
    save_data(recv_data, file_name)

    # 接受服务器放回的数据并存放在本地
    # 关闭套接字
    

if __name__ == "__main__":
    main()
