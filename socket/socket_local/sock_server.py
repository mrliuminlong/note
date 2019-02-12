#本地套接字　 本地两个文件交互
# linux 文件分类　b块设备 c字符设备 d目录 -普通文件 l链接 s套接子文件 p管道文件
from socket import *
#创建本地套接字
sockfd = socket(AF_UNIX, SOCK_STREAM)
# 绑定套接字文件
sockfd.bind("./sock")
sockfd.listen(5)
print("Waiting....")
while True:
    c, addr = sockfd.accept()
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
    c.close()
sockfd.close()
