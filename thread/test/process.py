#代码效率测试　多进程
from test import *
import threading
import time
import multiprocessing as mp

# def io():
#     write()
#     read()
jobs = []
t = time.time()
for i in range(10):
    p = mp.Process(target=count, args=(1,1))
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()
print("MutiProcess time:",time.time()-t)