from multiprocessing import Queue,Process
import time
#创建消息队列
q = Queue()
def fun1():
    for i in range(5):
        time.sleep(1)
        q.put(('a','b'))#放消息端
def fun2():
    for i in range(8):
        time.sleep(1.5)
        a,b = q.get()#读消息端
        print("sum=",a+b)
p1 = Process(target = fun1)#创建进程１
p2 = Process(target = fun2)#创建进程２
p1.start()
p2.start()
p1.join()
p2.join()