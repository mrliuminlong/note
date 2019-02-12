#子进程先退出，　父进程没有处理子进程的退出状态，此时子进程变为僵尸进程, 
# 僵尸进程虽然结束，但其PID仍然存在，该僵尸进程占用内存资源
#linux 终端查询僵尸进程命令　ps aux
import os 
import time
pid = os.fork()
if pid < 0:
    print("error")
elif pid == 0:
    print()
    print("child PID",os.getpid())
    print("get parent PID",os.getppid())
else:
    time.sleep(2)
    print("parent PID",os.getpid())
    print("get child PID",pid)