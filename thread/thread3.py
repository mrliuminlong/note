#线程属性示例
from threading import Thread,currentThread
from time import sleep

def fun():
    print("当前线程",currentThread().getName())
    sleep(3)
    print("线程属性")
#创建线程属性
t = Thread(target=fun)
t.setName("liu")#设置线程名字
t.start()

#线程名称

t.getName()#获得线程名字
t.is_alive()#线程状态
print("name:",t.name)
t.join()

# threading.currentThread()#在线程函数中获取当前线程对象