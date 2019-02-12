#使用multiprocessing 创建进程，同样子进程复制父进程的全部代码
#　　父子进程执行过程互不影响，各自有各自的执行空间，子进程只执行函数部分

import multiprocessing as mp 
from time import sleep 

a = 1
#编写进程函数
def fun ():
    sleep(3)
    global a#修改的a与父进程没有任何关系，属于子进程的a
    a = 10000
    print("a=",a )
    print("子进程事件")
#创建进程对象 方法
p = mp.Process(target = fun)

#启动进程
p.start()
sleep(4)
print("父进程事件")
#回收进程　join是阻塞函数　一定要在子进程结束后　才运行父进程
#join可以避免僵尸进程的产生
# p.join()
print("a=",a)
# sleep(4)
# print("父进程事件")
while True:
    pass
