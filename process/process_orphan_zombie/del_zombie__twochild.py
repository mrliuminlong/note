#创建二级子进程　处理僵尸进程
#  父进程创建子进程等待子进程退出
#  子进程创建二级子进程后立即推出　将事件交由父进程和二级子进程完成
#  一级进程被回收　二级进程变为孤儿进程
import os
from time import sleep
def f1():
    sleep(3)
    print("事件一　．．．．")
def f2():
    sleep(4)
    print("事件二．．．．")
pid = os.fork()
if pid < 0:
    print("error")
elif pid==0:
    p = os.fork()#创建二级子进程
    if p ==0:
        f2()#二级子进程完成事件
    else:
        os._exit(0)#一级子进程退出
else:
    os.wait()#等待回收一级子进程
    f1()