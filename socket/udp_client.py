from socket import *
import sys
# 命令行传入参数
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)
# 创建套接字
client = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input("Msg>>")
    if not data:
        break
    client.sendto(data.encode(),ADDR)
    msg,addr = client.recvfrom(1024)
    print("From server:",msg.decode(),addr)
client.close()