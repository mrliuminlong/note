#multiprocessing 中父进程主要来创建和管理子进程，其它事件子进程完成
#join 回收子进程，避免僵尸进程的产生

import multiprocessing as mp
from time import sleep
import os

def th1():
    sleep(3)
    print("起床")
    print(os.getppid(),"-----",os.getpid())
def th2():
    sleep(5)
    print("吃饭")
    print(os.getppid(),"-----",os.getpid())
def th3():
    sleep(8)
    print("python")
    print(os.getppid(),"-----",os.getpid())
def th4():
    sleep(9)
    print("go home")
    print(os.getppid(),"-----",os.getpid())
# def th1():
#     sleep(3)
#     print("起床")
#     print(os.getppid(),"-----",os.getpid())

things = [th1, th2, th3, th4]
process = []
#创建多个进程对象
for th in things:
    p = mp.Process(target = th)
    process.append(p)
    #启动子进程
    p.start()
#保留进程对象一起回收
for i in process:
    i.join()
