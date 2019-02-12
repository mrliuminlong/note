#向服务端发送请求　request
# from socket import *
# s = socket()
# s.bind(('0.0.0.0',8000))
# s.listen(5)
# print("waiting....")
# c,addr = s.accept()
# print("Connectting.....",addr)
# print("----------------------------")
# while True:
#     data = c.recv(20)
#     if not data:
#         break
#     print(data)
# print("----------------------------")
# c.close()
# s.close()
from socket import *
client = socket()
ARRD = ('127.0.0.1',8000)
client.connect(ARRD)
while True:
    data = c.recv(4096)
    if not data:
        break
    client.send(data)