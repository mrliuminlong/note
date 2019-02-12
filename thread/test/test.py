#  from threading import Thread

#  #创建线程
#  t = Thread(target = fun, args)#绑定函数，　args 元组传参　kwargs字典传参　name 线程名称
#  t.start()
#  t.join([timeout])#回收线程

#计算密集型程序
def count(x,y):
    c = 0
    while c <7000000:
        x += 1
        y += 1
        c += 1

#IO密集型程序
def write():
    f = open("test","w")
    for i in range(1200000):
        f.write("hello world\n")
    f.close()
def read():
    f = open("test")
    lines = f.readlines()
    f.close

#测试程序
