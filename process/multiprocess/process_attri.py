# 对象属性
# p.name 进程名称　p.pid 进程PID号　　P.is_alive() 查看进程状态
from multiprocessing import Process
from time import ctime, sleep



def tm():
    for i in range(4):
        sleep(2)
        print(ctime())
p = Process(target = tm, name = "liu")
p.start()
print("Process name:",p.name)
print("Process PID:",p.pid)
print("Process alive:",p.is_alive())

p.join()

 
# text_file="/home/tarena/aid1811/python_net/multiprocess/test.txt"
# #open()
# f=open(text_file,"r")
# #seek() 确定读文件指针位置
# f.seek(8,0)
# #tell 告诉当前指针位置
# pos=f.tell()
# #read()　读多少字节
# text_to_number=f.read(50)
# # f.seek(8,1)
# text_to_all=f.read()
 
# f.close()
 
# print(pos)
# print(text_to_number)
