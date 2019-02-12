from threading import Thread,Lock
#GIL 全局解释器锁　同一时刻只有一个线程被解释，直接导致Python的线程运行效率低下

a = b =0
lock = Lock()
def value():
    while True:
        lock.acquire()#临界区代码进行加锁
        if a != b:
            print("a = %d,b=%d"%(a,b))
        lock.release()#解锁
t = Thread(target=value)
t.start()
while True:
    with lock:#加锁
        a += 1
        b += 1

t.join()