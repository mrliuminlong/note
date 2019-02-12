from socket import *
import time
import sys,os
from threading import Thread,currentThread
from multiprocessing import Process 
import signal #信号处理模块　帮助处理僵尸进程
# 导入signal模块　在父进程中运行
#非阻塞函数　这样父进程在有子进程退出，则将子进程交系统处理　linux unix系统下运行


#创建套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
ADDR = (('0.0.0.0', 8888))
s.bind(ADDR)
s.listen(5)
#忽略子进程退出释放资源，交给系统处理子进程，避免僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
FILES = ("/home/tarena/abc/")

def handler(c):
    print("Connect ...",c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send("Thank your msg:".encode())
    c.close()
    #线程时候不用加sys.exit()因为线程函数执行完毕就退出，而进程不一样
    sys.exit(0)#客户端退出　子进程退出

#接收客户端请求
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务器退出")
    except Exception as e:
        print("服务器异常：",e)
        continue
#     #创建线程
#     t = Thread(target=handler, args=(c,))
#     t.setDaemon(True)#守护进程　主进程退出所有线程退出　避免使用join()函数　如果使用join会使得主进程关闭
#     t.start()

#将线程改为创建进程
    p = Process(target=handler, args=(c,))
    p.daemon = True
    p.start()
