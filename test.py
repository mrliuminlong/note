# import os
# from time import *

# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:

# pid = os.fork()
# print(pid)
# if pid == 0:
#     # print("child process",os.getpid(),os.getppid())
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
    # print("parent process",os.getpid())


# from multiprocessing import Process
# import os

# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__=='__main__':
#     print('Parent process %d' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')


# from multiprocessing import Pool
# import os, time, random

# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     # time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(5)
#     for i in range(6):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')


# import time
# from multiprocessing import Pool
 
 
# def run(count):
# 	print('子进程编号:%s' % count)
# 	time.sleep(2)
# 	print('子进程%s结束' % count)
 
 
# if __name__ == "__main__":
# 	print("开始执行主程序")
# 	start_time = time.time()
# 	# 使用进程池创建子进程
# 	pool = Pool(4)
# 	print("开始执行子进程")
# 	for i in range(4):
# 		pool.apply_async(run, (i,))
# 	pool.close()
# 	pool.join()
# 	# 进程池调用close方法后，会把进程池状态改为不可再插入元素的状态，但并未关闭进程池
# 	# close必须在join之前调用。
# 	# join()调用后主进程必须等子进程全部运行结束后才接着运行主进程。
# 	print("主进程结束耗时%s" % (time.time() - start_time))

# import subprocess

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# # print('Exit code:', r)

# from multiprocessing import Process, Queue
# import os, time, random

# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())

# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)

# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()
import gevent 
from gevent import monkey#导入到本地
monkey.patch_all()
#脚本运行必须在模块导入之前
#运行monkey 脚本可以使得程序中的阻塞可以被gevent捕获
from socket import *

#创建套接字
def run_server():
    server = socket()
    server.bind(('0.0.0.0',8888))
    server.listen(10)
    while True:
        childserver, addr = server.accept()
        print("Connect from",addr)
        #handle(client)
        gevent.spawn(handle,childserver)#协程方案

def handle(client):
    while True:
        data = childserver.recv(1024)
        if not data:
            break
        print(data.decode())
        childserver.send(b'ok')
    childserver.close()

run_server()