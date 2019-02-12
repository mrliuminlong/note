# os.getpid() 获取当前进程的PID号　返回值PID号
import os 
import time
pid = os.fork()
if pid < 0:
    print("error")
elif pid == 0:
    print("child process",os.getpid())
else:
    time.sleep(2)
    print("parent process",os.getpid())