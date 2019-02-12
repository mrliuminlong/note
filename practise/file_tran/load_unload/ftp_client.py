
import os,sys
from socket import *
import time

FILES = "/home/tarena/file/"
#具体请求功能
class FtpClient(object):
    def __init__(self,s):
        self.s = s

    #查看文件列表
    def do_list(self,s):
        self.s.send(b"L")#发送请求
        data = self.s.recv(128).decode()
        if data =="ok":
            data = self.s.recv(4096).decode()
            files = data.split('#')
            for file in files:
                print(file)
        else:
            print(data)#打印无法操作原因
    def do_quit(self):
        self.s.send(b"Q")
        self.s.close()
        sys.exit("谢谢使用")
    def do_get(self, FILES, filename):
        self.s.send(('G '+filename).encode())
        data = self.s.recv(128).decode()
        if data == "ok":
            fd = open(FILES+filename,'wb')
            while True:
                data = self.s.recv(1024)
                if data == b"##":
                    break
                fd.write(data)
            fd.close()
            print("文件下载完毕")
        else:
            print(data)
    def do_put(self, FILES, filename):
        try:
            f = open(FILES+filename, 'rb')
        except Exception:
            print("没有找到文件")
            return
        # filename = filename.split('/')
        self.s.send(('P '+filename).encode())
        data = self.s.recv(128).decode()
        if data =="ok":
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.s.send(b'##')
                    break
                self.s.send(data)               
            f.close()
            print("文件上传完毕")
        else:
            print(data)

#网络连接
def main():
    if len(sys.argv) < 3:
        print("argv is wrong")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)
    #创建套接字
    s = socket()
    try:        
        s.connect(ADDR)#连接
    except Exception as e:
        print("连接服务器失败：",e)
        return
    ftp = FtpClient(s)#创建实例对象
    while True:
        print("\n======= 命令选项  ==========")
        print("======     list      ========")
        print("======   get file    ========")
        print("======   put file    ========")
        print("======     quit      ========")
        print("=============================\n")
        cmd = input("输入命令>>")
        # print(cmd)
        if cmd.strip() == "list":
            ftp.do_list(s)
        elif cmd.strip() =="quit":
            ftp.do_quit()
        elif cmd[:3] == 'get':
            filename = cmd.split(" ")[-1]
            ftp.do_get(FILES,filename)
            print("文件名：",filename)
        elif cmd[:3] == 'put':
            filename = cmd.split(" ")[-1]
            ftp.do_put(FILES,filename)
        else:
            print("请输入正确命令")

        

main()