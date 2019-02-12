#p.daemon 默认为False 表示主进程退出，不会影响子进程的执行
#       设置为True 表示主进程退出，子进程也会退出
#必须在start 前设置　
#守护进程　linux 是和操作系统相进退
from multiprocessing import Process
from time import ctime, sleep



def tm():
    for i in range(4):
        sleep(2)
        print(ctime())
p = Process(target = tm, name = "liu")
p.daemon = True
p.start()
print("Process name:",p.name)
print("Process PID:",p.pid)
print("Process alive:",p.is_alive())

p.join()
