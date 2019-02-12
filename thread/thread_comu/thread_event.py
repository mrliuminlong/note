from threading import Thread,Event
from time import sleep

s = None#设置为全局变量，此示例为通信
e = Event()
def bar():
    print("Bar拜山头")
    sleep(1)
    global s
    s = "天王盖地虎"
    e.set()

b = Thread(target=bar)
b.start()
print("说对口令就是自己人")
e.wait()#阻塞等待，分支线程set
if s == "天王盖地虎":
    print("自己人")
else:
    print("打死他")

