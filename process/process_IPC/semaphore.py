#信号量(信号灯)　给定一个数量　多个进程都可以见到　
# 多个进程可以操作信号量的增加和消耗　来达到协同工作
from multiprocessing import Semaphore, Process
import os
from time import sleep
# sem = Semaphore(num)#创建信号量对象　信号量初始值　返回值　信号量对象
# sem.acquire()#将信号量减1　如果信号量为零则为阻塞
# sem.release()#将信号量加1
# sem.get_value()#获取信号量数量


#创建初始信号量
sem = Semaphore(3)
def fun():
    print("%d想执行事件"%os.getpid())
    sem.acquire()
    print("%d事件执行．．．．"%os.getpid())
    sleep(3)
    print("%d执行完毕"%os.getpid())
    print("信号量剩余：",sem.get_value())
    sem.release()#执行完毕后添加一个信号量
jobs = []
#5个进程想执行
for i in range(5):
    p = Process(target = fun)
    jobs.append(p)
    p.start()

for i in range(5):
    p.join()