from socket import *
from time import sleep

station = ('176.234.83.255',8888)
send = socket(AF_INET, SOCK_DGRAM)
send.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
print("广播开始啦！")
while True:
    sleep(3)
    send.sendto("人在江湖，一路平安！".encode(),station)
send.close()
