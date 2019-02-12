import os 
import time
pid = os.fork()
if pid < 0:
    print("error")
elif pid == 0:
    print()
    print("child PID",os.getpid())
    print("get parent PID",os.getppid())
    os._exit(0)
else:
    print("parent PID",os.getpid())
    while True:
        time.sleep(2)

#终端显示　python aux child PID
'''如何处理僵尸进程
1.父进程中使用函数处理子进程退出
返回值：pid 退出子进程的PID　status
'''