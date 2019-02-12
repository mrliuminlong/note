#共享内存　通信原理　在内存中开辟一个空间，对多个进程可见，多个进程均可读写内容，
#  　　　　但是每次读写内容都会覆盖前次内容

from multiprocessing import Value, Array,Process

#开辟共享内存空间 ctype字符串　表示共享内存中存的数据类型('i','f','c')　obj表示共享内存的初始化数据
# obj = value(ctype, obj)
# obj.value 对该属性的修改和使用即对共享内存的内容读写

#模拟进账和出帐的过程
import time
import random

#创建初始的资金
money = Value('i', 10000)

#挣钱过程
def boy_makemoney():
    for i in range(30):#按一月３０天计算
        time.sleep(0.2)
        #对value 属性操作　即对共享内存操作
        money.value += random.randint(1, 1000)#每日进账1~1000不等

def girl_spendmoney():
    for i in range(30):
        time.sleep(0.2)
        money.value -= random.randint(100,900)#每日花费100～900

b = Process(target = boy_makemoney)
g = Process(target = girl_spendmoney)
b.start()
g.start()
b.join()
g.join()
print("一月余额：",money.value)