#导入 socket、sys 模块
from socket import * 
import time

client = socket()
server_addr = ('127.0.0.1',8888)
client.connect(server_addr)

while True:
    data = input("输入消息：")
    if not data:
        break
    client.send(data.encode())
    data = client.recv(1024)
    time.sleep(1)
    print("From serve:",data.decode())
client.close()
        