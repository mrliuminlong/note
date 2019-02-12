# class Process(object):
#     def __init__(self, pid)
#     self.pid = pid
#继承Process
# from multiprocessing import Process
# class MyClass(Process):
#     def __init__(self, value):
#         self.value = value
#         super(MyClass, self).__init__()
#     def run(self):
#         return self.value
# p = MyClass(20)
# r = p.run()
# print(r)
# p.start()
# p.join()
Pipe()#创建管道　fd.recv() fd.send() 双向管道　和单项管道
Queue()#消息队列　主要指进程间通信　q.get() q.put() q.full() q.close() q.qsize()