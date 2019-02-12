#客户端处理函数
def client_handler(c):
    print("客户端:",c.getpeername())
    while True:
        data = c.recv(1024)
        print(data.decode())
        c.send(b'Thank you!')
        if not data:
            break
    c.close()