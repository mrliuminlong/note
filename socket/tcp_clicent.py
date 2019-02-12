from socket import *
ADDR = (('127.0.0.1',8888))
client = socket()
client.connect(ADDR)
while True:
    data = input("Msg>>")
    if not data:
        break
    client.sendto(data.encode(),ADDR)
    msg,addr = client.recvfrom(1024)
    print("From server:",msg.decode(),addr)
client.close()