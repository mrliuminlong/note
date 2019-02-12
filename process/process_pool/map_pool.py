#
from multiprocessing import Pool
import time
def fun(n):
    time.sleep(1)
    return n**2

pool = Pool()
#使用map函数将事件放入返回池
r = pool.map(fun, [1,2,3,4,5])
pool.close()
pool.join()
print(r)