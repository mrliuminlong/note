import os
from time import sleep
# 子进程从fork下一句执行
# 子进程与父进程运行互不影响，使用同一终端，运行顺序不定
# 子进程复制父进程的所有空间和语句,但是父子进程各自空间独立，操作各自空间互不影响
#进入阻塞状态的进程一定会让出cpu时间片段
#子进程有自己特有的PID, PCD,命令集
# if ...elif....else....结构正是根据父子进程返回值不同让父子进程执行不同的内容，是fork函数固定搭配
print("================")
a = 1
pid = os.fork()#创建新进程　　失败返回一个负数;　成功在原进程返回新进程PID　新进程返回0
if pid < 0:
    print("Create process failure!")
elif pid ==0:
    print("child process!")
    a = 10000
    print("child process:a = %d"%a)
    
else:
    sleep(1)
    print("parent process")
    print('parent a:',a)
print("fork test end...")