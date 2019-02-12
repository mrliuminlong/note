# multilpocessing 的传参数
from multiprocessing import Process
from time import sleep
def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I'm  %s"%name)
        print("I,m working...")

p = Process(target = worker, args=(2, 'Qevi'))#位置传参数 第一种传参
# p = Process(target = worker, kwargs={'sec':2, "name":"Levi"})#按键的名称传递参数　第二种传参
p = Process(target = worker, args = (2,),\
kwargs={"name":"Devi"})#按键的名称传递参数　第三种传参

p.start()
p.join()