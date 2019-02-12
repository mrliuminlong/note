'''
本例复制文件　复制的文件分为上下部分，分开复制
＠liu
2019-01-30修改
星期三
离农历猪年差５天了
为什么父进程复制不上文件???/
'''

import os
import time
filename = "/home/tarena/aid1811/python_net/practise/file_tran/copy/image.jpg"
#获取文件大小
size = os.path.getsize(filename)
#创建进程
pid = os.fork()
if pid < 0:
    print("error")
elif pid ==0:
    #复制上半部分
    f = open(filename,'rb')
    #打开另一个文件
    fw = open("child.jpg","wb")
    #将文件分开两半
    n = int(size // 2)
    while True:
        if n < 1024:
            data = f.read(n)
            fw.write(data)
            #关闭文件
            f.close()
            fw.close()
            break
        else:
            data = f.read(1024)
            fw.write(data)
            n-=1024        
else:
    #让父进程停止１秒
    time.sleep(1)
    #复制下半部分
    f = open(filename,'rb')
    fw = open("parent.jpg",'wb')
    f.seek(size//2,0)#文件指针　或者偏移量　正向后　负向前
    while True:
         if n < 1024:
            data = f.read(n)
            fw.write(data)
            f.close()
            fw.close()
            break
         else:
            data = f.read(1024)
            fw.write(data)
            n-=1024 
    # while True:
    #     data = f.read(1024)
    #     fw.write(data)
    #     if not data:
    #         break
    f.close()
    fw.close()