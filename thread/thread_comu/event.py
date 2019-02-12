from threading import Event
#创建事件对象
e = Event()
e.set()#设置e,就不阻塞了
e.wait(3)#设置阻塞时间　
e.clear()#清除后就再次阻塞
e.is_set()
print("------------")