#t.daemon 默认False 表示主线程退出不影响分支线程执行，设置为True　则主线程和分子线程都退出
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
t.setDaemon(True)
print("Daemon:",t.isDaemon())
t.start()
#需要在start前设置daemon属性，通常不会和join()一同使用
#线程名称


t.join()

# threading.currentThread()#在线程函数中获取当前线程对象