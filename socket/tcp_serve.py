
import socket
import time
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0',8888))
server.listen(5)

while True:
    print("Waiting  ")
    server_1,addr = server.accept()
    print("Connect from client:",addr)    
    while True:
        data = server_1.recv(1024)
        if not data:
            break
        print("Server_1 receive message:",data.decode())
        time.sleep(1)
        answer = server_1.send(b"I see!")
        print("Server_1 reply %d bytes" % answer)
    client.close()
server.close()


