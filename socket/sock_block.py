from socket import *
from time import sleep, ctime
sockfd = socket()
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(5)
# sockfd.setblocking(False)#设置为非阻塞　True 设置为阻塞
sockfd.settimeout(5)
n = 0
while True:
    print("waiting for connect.....")
    try:
        connfd,addr =sockfd.accept()
    except timeout:
        print("等不起．．．")
    except BlockingIOError:
        sleep(2)
        n += 2
        print("bnlocking waiting%dsec"%n,ctime())#打印阻塞等待多少秒
    else:
        print("Connecting from",addr)
        data = sockfd.recv(1024)
        print("Receive",data.decode())
        n = 0