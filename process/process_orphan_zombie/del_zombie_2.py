#如何处理僵尸进程 2
#父进程中使用函数处理子进程退出pid, status = os.waitpid(pid, optin).  返回值：pid status 
#pid ＞0表示等待指定PID子进程退出　pid=-1 表示等待任意子进程退出
# status =0 表示阻塞等待　status=WNOHANG　表示非阻塞
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
    pid, status = os.wait() #　阻塞等待处理子进程退出
    print(" 　exited child pid",pid)#退出的子进程PID
    print("status:",status)#子进程退出状态
    print("　 parent PID",os.getpid())
    while True:
        time.sleep(2)