from socket import *
from multiprocessing import *
import os,sys
from client_handler import *


HOST = "0.0.0.0"
PORT = 8888
ADRR = (HOST,PORT)
#创建套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADRR)
s.listen(5)
#循环等待客户端请求
print("Listening to the port 8888")
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("退出服务器")
    except Exception as e:
        print("Error:",e)
        continue
    #创建新的进程，处理客户端请求
    pid = os.fork()
    if pid == 0:
        p = os.fork()
        if p == 0:#二级子进程 避免僵尸进程
            s.close()
            client_handler(c)#处理具体请求
            sys._exit(0)#子进程处理完请求即退出
        else:
            os._exit(0)
    #父进程或者创建进程失败，都是等待下一个客户端连接
    else:
        c.close()
        os.wait()

