#获取父进程的PID 返回父进程的PID
import os 
import time
pid = os.fork()
if pid < 0:
    print("error")
elif pid == 0:
    time.sleep(1)
    print()
    print("child PID",os.getpid())
    print("get parent PID",os.getppid())
else:
    # time.sleep(2)
    print("parent PID",os.getpid())
    print("get child PID",pid)