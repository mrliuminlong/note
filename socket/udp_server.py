from socket import *

server = socket(AF_INET, SOCK_DGRAM)
server.bind(("0.0.0.0",8889))
print("waiting!")
while True:
    data,addr = server.recvfrom(1024)
    if not data:
        break
    print("Server receive message %s:%s"%(data.decode(),addr))
    server.sendto(b"Thank for your msg!",addr)
server.close()
