#导入 socket、sys 模块
# from socket import * 
# import time

# client = socket()
# server_addr = ('127.0.0.1',8888)
# client.connect(server_addr)
# count = 0
# while True:
#     data = input("输入消息：")
#     if not data:
#         break
#     client.send(data.encode())
#     data = client.recv(1024)
#     time.sleep(1)
#     print("From serve:",data.decode())
# client.close()


from socket import *
from time import time

client = socket()
ADDR = ('127.0.0.1',8888)
client.connect(ADDR)
while True:
    data = input("客户端输入信息：")
    if not data:
        break
    client.send(data.encode())
    data = client.recv(1024)
    print("收到服务端回应：",data.decode())
client.close()
