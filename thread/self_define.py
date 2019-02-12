#继承Thread
#编写__init__添加属性，　加载父类＿init__
#重写run方法

from threading import Thread
from time import sleep,ctime
#自定义类

# class MyThread(Thread):
#     def __init__(self,target,args=(),kwargs={},name="tedu"):
#         super(MyThread, self).__init__()
#         self.target = target
#         self.args = args
#         self.kwargs = kwargs
#         self.name = name
#     def run(self):
#         self.target(*self.args, **self.kwargs)

#测试函数
def player(sec, song):
    for i in range(2):
        print("Playing %s:%s"%(song,ctime()))
        sleep(sec)

t = Thread(target=player, args=(3,), kwargs={"song":"天亮了"}, name="tedu")
t.start()
t.join()

