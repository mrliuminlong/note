from socket import *
import sys
# 命令行传入参数
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)
# 创建套接字
client = socket(AF_INET, SOCK_DGRAM)

while True:
    # def show():
    print("成功登录银行客户端")
    data = input("请输入帐号：")
    if not data:
        break
    client.sendto(data.encode(),ADDR)
    msg,addr = client.recvfrom(1024)
    print("余额:",msg.decode())
client.close()