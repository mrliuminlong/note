import threading
from time import sleep
import os

# #线程函数
# def music():
#     for i in range(5):
#         sleep(2)
#         print("播放音乐",os.getpid())

# #创建线程对象
# t = threading.Thread(target = music)
# t.start()

# #主线程运行
# for i in range(3):
#     sleep(3)
#     print("雪莲花",os.getpid())
# t.join()

# 线程函数
a = 1
def music():
    for i in range(5):
        global a
        a = 100
        sleep(2)
        print("a=",a)

#创建线程对象
t = threading.Thread(target = music)
t.start()

#主线程运行
for i in range(3):
    sleep(3)
    print("雪莲花a=",a)
t.join()