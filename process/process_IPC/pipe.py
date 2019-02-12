from multiprocessing import Pipe, Process
import time
import os
#创建管道
fd1, fd2 = Pipe()
def fun(name):
    time.sleep(3)
    fd1.send(name)
jobs = []
#子进程发消息
s = "ABCDEGF"
for i in s:
    p = Process(target= fun, args =(i,))
    jobs.append(p)#列表中放函数
    # print(p.pid)
    p.start()
#父进程从管道读消息
# for i in range(5):
while True:
    data = fd2.recv()
    print("父进程",data)
    if not data:
        break

for i in jobs:
    i.join()