#共享内存
#obj  = Array(ctype, obj) 
# ctype字符串　表示数据类型　
# obj 存入结构化数据（列表，bytes)表示初始数据;传入整型，表示开辟多大空间
#返回值　共享内存对象
#可以通过遍历获得共享内存的每一个值，同时支持索引操作

from multiprocessing import Process,Array
import time

shm = Array('i',[1,2,3,4])
def fun():
    for i in shm:
        print(i)
    shm[0] = 1000#修改共享内存

p = Process(target = fun)
p.start()
p.join()

for i in shm:
    print(i)#父进程数据修改

# #开辟空间
# from multiprocessing import Process,Array
# import time

# shm = Array('i',5)#开辟5个空间
# def fun():
#     for i in shm:
#         print(i)
#     shm[0] = 1000#修改共享内存

# p = Process(target = fun)
# p.start()
# p.join()

# for i in shm:
#     print(i)#父进程数据修改

#存入字符串
# from multiprocessing import Process,Array
# import time

# shm = Array('c',b"Hello")#字符串
# def fun():
#     for i in shm:
#         print(i)
#     #修改共享内存 必需传入字符串
#     shm[0]='A'
# p = Process(target = fun)
# p.start()
# p.join()

# for i in shm:
#     print(i)#父进程数据修改

# print(shm.value)#打印字符串

