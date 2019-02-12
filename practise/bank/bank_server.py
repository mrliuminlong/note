from socket import *
from bank_mysql import *
server = socket(AF_INET, SOCK_DGRAM)
server.bind(("0.0.0.0",8888))
s =Bank('622345000002')
# print(s)
print("waiting!")
while True:
    data,addr = server.recvfrom(1024)
    if not data:
        break
    print("客户登录：帐号%s, 地址%s"%(data.decode(),addr))
    # print(data)
    # print(str(data))
    s = Bank(data.decode()) 
    server.sendto(str(s).encode(),addr)
    # server.sendto(b"hello!",addr)
server.close()
