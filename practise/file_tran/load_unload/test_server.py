'''
ftp文件传输编程
服务器端
＠liu
2019-01-19
学习到了　fork 是在linux下的特有函数　　可以创建子进程是自身，也可以不是自身
multiprocessing 是可以跨平台用的模块　可以调用外部函数
os.listdir()函数返回是列表，想将其转字符串，可以用for语句读出，
　　　每次读出中间加"#"for循环执行结束，可以形成一整串的字符串，
str.split()是字符串转列表
超出索引范围的切片，会报错
apply_asyn（）异步函数，子进程可以部分先后同时执行
'''
import os,sys
from socket import *
import time
#将文件处理过程封装
#完成构架

def request(connfd,data,FILES):
    if data.decode()=="list":
        # connfd.send("欢迎查询：".encode())
        #获取文件列表
        file_list = os.listdir(FILES)
        # print(file_list)
        files = ""
        if not file_list:
            connfd.send("文件目录为空".encode())
            return
        else:
            for file in file_list:
                files = files+file+"#"
                # print(files)
            connfd.send(files.encode())

    elif data.decode()=="quit":
        connfd.send("欢迎下次光临,服务端退出！".encode())
        connfd.close()
        sys.exit("服务端退出")                
    else:
        data = data.decode().split(" ")
        if data[0]=="get":
            file = FILES + data[1]
            with open(file,'rb') as f:
                while True:
                    data = f.read(1024)
                    connfd.send(data)
                    if not data:
                        break
        # elif data[0]=="put": 
        #     file = FILES + data[1]
        #     print("客户端上文件名",data[1])
        #     with open(file,"wb") as f:
        #         while True:
        #             data = f.write(1024)
        #             connfd.send(data)
        #         if not data:
        #             break


def main():
    #创建全局变量
    HOST = ('0.0.0.0')#IP
    PORT = 8889#端口
    ADDR = (HOST,PORT)#地址
    FILES = '/home/tarena/abc/'#文件库
    #创建套接字　建立网络链接
    sockfd = socket()
    #创建多次链接
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    #绑定链接
    sockfd.bind(ADDR)
    #监听
    sockfd.listen(3)
    #建立循环链接
    print("等待链接，监听....")
    while True:
        try:
            connfd, addr = sockfd.accept()#建立链接
            print("链接客户端成功，地址：",addr)
        except Exception as e:
            print("异常：",e)
        pid = os.fork()#创建子进程
        if pid == 0: 
            sockfd.close()                    
            while True:    
                data = connfd.recv(1024)
                print(data.decode())  
                request(connfd,data,FILES)
        else:
            connfd.close()
                
main()

        
        
        