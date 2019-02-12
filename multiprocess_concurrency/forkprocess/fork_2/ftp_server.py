'''
ftp文件服务程序
fork server 训练
＠liu
2019-01-17
'''
import os, sys
from socket import *
import time

#将文件处理过程封装
class FtpServer():
    def __init__(self,connfd):
        self.connfd = connfd

    def do_list(self,connfd):
        print("执行List")
        #获取文件列表
        file_list = os.listdir(FILES)
        if not file_list:
            self.connfd.send("文件库目录为空".encode())
            return
        else:
            self.connfd.send(b"ok")
            time.sleep(0.1)
        files = ""
        for file in file_list:
            if file[0] != "." and os.path.isfile(FILES + file):#判断不是隐藏文件(._)
                files = files +file + "#"
        self.connfd.send(files.encode())

    def do_get(self, filename):
        try:
            fd = open(FILES+filename, 'rb')
        except Exception:
            self.connfd.send("文件不存在".encode())
            return

        self.connfd.send(b"ok")
        time.sleep(0.1)
        #循环发送文件内容
        while True:
            data = fd.read(1024)
            #到文件结尾
            if not data:
                time.sleep(0.1)
                self.connfd.send(b"##")
                break
            self.connfd.send(data)
    def do_put(self, filename):
        if os.path.exists(FILES+filename):
            self.connfd.send("文件存在".encode())
            return
        try:
            fd = open(FILES+filename, 'wb')           
        except:
            self.connfd.send("上传失败".encode())
            return
        else:
            self.connfd.send(b'ok')
        while True:
            data = self.connfd.recv(1024)
            if data == b"##":
                break
            fd.write(data)
        fd.close()
        print("文件接收上传完毕")

#IP地址
HOST = '0.0.0.0'
PORT = 8888
ADDR =(HOST, PORT)
FILES = "/home/tarena/abc/"
#封装并发网络模型
def main():
#创建服务端套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)
    print("listen to 8888.....")

    while True:
        try:
            connfd, addr = s.accept()
        except KeyboardInterrupt:#客户端退出
            s.close()
            sys.exit("服务器退出！")
        except Exception as e:
            print("服务端异常：",e)
            continue
        print("连接到客户端：",addr)
        #创建子进程
        pid = os.fork()
        if pid == 0:
            p = os.fork()#创建２级子进程　避免僵尸进程
            if p == 0:
                s.close()
                #根据客户端请求执行操作 1查找　2下载文件　3上传文件 q 退出
                ftp = FtpServer(connfd)#实例化对象
                while True:
                    #接收请求
                    data = connfd.recv(1024).decode()
                    print("服务端接收data:",data)
                    if not data or data[0] == "Q":#如果客户端空格回车　或者输入Q 
                        connfd.close()
                        sys.exit("客户端退出")
                    elif data[0]== "L":
                        ftp.do_list(connfd)
                    elif data[0] == 'G':
                        filename = data.split(" ")[-1]
                        print("服务端接收的文件名:",filename)
                        ftp.do_get(filename)
                    elif data[0] == 'P':
                        filename = data.split(" ")[-1]
                        print("服务端接收上传的文件名:",filename)
                        ftp.do_put(filename)                                 
            else:
                os._exit(0)
        else:
            connfd.close()
            os.wait()
main()