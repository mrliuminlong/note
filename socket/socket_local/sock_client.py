#本地套接字
from socket import *
sockfd = socket(AF_UNIX, SOCK_STREAM)
#两端需要使用相同的套接字文件
sockfd.connect("./sock")
while True:
    msg = input(">>")
    if not msg:
        break
    sockfd.send(msg.encode())
sockfd.close()

# os.remove(file)删除一个文件
# os os.path.exists()判断一个文件是否存在