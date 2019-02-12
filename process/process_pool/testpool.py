#创建进程池
from multiprocessing import Pool
from time import sleep,ctime

def worker(msg):
    sleep(2)
    print(msg)
    return ctime()
# 创建进程池对象 进程数量默认根据系统自动判定
pool = Pool()
result = []
for i in range(10):
    msg = "hello %d"%i
    # r = pool.apply_async(func=worker, args=(msg,))
    
    r = pool.apply(func=worker, args=(msg,))#同步执行
    result.append(r)
# pool.apply_async(func, args, kwds)
#使用进程池中的进程执行函数事件　参数func要执行函数(必须在进程池创建之前声明)　
# args 元组给func位置传参　kwds字典　给func键值传参
#关闭进程池
pool.close()
#回收进程池
pool.join()
for i in result:
    print(i.get())#获取进程事件函数的返回值