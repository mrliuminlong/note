# 当父进程退出　子进程被称为孤儿进程，该孤儿进程被系统进程收养
import os 
import time
pid = os.fork()
if pid < 0:
    print("error")
elif pid == 0:
    time.sleep(1)#子进程暂停1秒，　父进程先执行完毕，该子进程变为孤儿进程
    print()
    print("child PID",os.getpid())
    print("get parent PID",os.getppid())
else:
    # time.sleep(2)
    print("parent PID",os.getpid())
    print("get child PID",pid)