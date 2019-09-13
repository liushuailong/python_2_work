import socket 
import threading


def recv_data(thread_socket):
    while True:
        recv_datas = thread_socket.recvfrom(1024)
        print("收到来自客户端{}的消息:{}".format(recv_datas[1], recv_datas[0].decode("utf-8")))


def send_data(thread_socket):
    while True:
        send_datas = input("请您发送输入的数据：")
        thread_socket.sendto(send_datas.encode("utf-8"), ("192.168.0.105", 8080))
    


def main():
    #创建UTP 套接字
    thread_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    thread_socket.bind(("", 8080))

    #src_addr
    # 接受数据
    # thread_socket.recvfrom(("192.168.0.103", 8080))
    # thread_socket.sendto(data,(ip,port))
    # 线程1 用来接受数据然后显示
    thread_1 = threading.Thread(target=recv_data, args=(thread_socket,))
    # 线程2 用来检测键盘数据然后通过udp发送数据
    thread_2 = threading.Thread(target=send_data, args=(thread_socket,))
    # 启动线程1和2
    thread_1.start()
    thread_2.start()
    # 关闭套接字
    # thread_socket.close()


if __name__ == "__main__":
    main()
