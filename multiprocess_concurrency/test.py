import gevent 
from gevent import monkey#导入到本地
monkey.patch_all()
#脚本运行必须在模块导入之前
#运行monkey 脚本可以使得程序中的阻塞可以被gevent捕获
from socket import *

#创建套接字
def run_server():
    server = socket()
    server.bind(('0.0.0.0',8888))
    server.listen(10)
    while True:
        childserver, addr = server.accept()
        print("Connect from",addr)
        #handle(client)
        gevent.spawn(handle,childserver)#协程方案

def handle(client):
    while True:
        data = childserver.recv(1024)
        if not data:
            break
        print(data.decode())
        childserver.send(b'ok')
    childserver.close()

run_server()