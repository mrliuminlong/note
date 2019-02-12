'''
ftp传输文件编程练习
客户端
＠liu
2019-01-19
'''
import os,sys
from socket import *
import time

#创建全局变量
FILES = '/home/tarena/file/'#创建客户端文件库
#创建socket套接字
client = socket()
ADDR = ('127.0.0.1',8889)#地址

def show():
    print("\n======= 命令选项  ==========")
    print("======     list      ========")
    print("======   get file    ========")
    print("======   put file    ========")
    print("======     quit      ========")
    print("=============================\n")

def do_list(client,text):
    client.send(text.encode())
    data = client.recv(1024)
    # print(data.decode())
    # for file in data.decode():
    #     print(file)
    # print(data.decode())
    files = data.decode().split('#')
    # print(files)
    for file in files:
        print(file)
def do_quit(client,text):
    client.send(text.encode())
    data = client.recv(1024)
    print(data.decode())
    sys.exit("客户端退出！")
def do_get(client,text,FILES):
    client.send(text.encode())
    text = text.split(" ")
    file = FILES + text[1]
    with open (file,'wb') as f:
        while True:
            data = client.recv(1024)
            f.write(data)
            if not data:                
                break
        print("下载完毕！")
        f.close()
# def do_put(client,text,FILES):
#     text = text.split(" ")
#     file = FILES + text[1]
#     try:
#         with open (file,'rb') as f:
#             while True:
#                 data = f.read(1024)
#                 client.send(data)
#                 if not data:                
#                     break
#             print("上传完毕！")
#             f.close()
#     except Exception as e:
#         print("上传文件操作有误")               

def main():
    try:
        client.connect(ADDR)#链接
        print("链接服务器成功！")
    except Exception as e:
        print("链接失败！")
    while True:
        show()   
        text = input("客户端：")
        text = text.strip()
        # print(text)
        if text =="list":
            do_list(client,text)
        elif text[:3] =="get" and text[3:]!="":
            do_get(client,text,FILES)
        # elif text[:3] =="put" and text[3:]!="":
        #     do_put(client,text,FILES)
        elif text =="quit":
            do_quit(client,text,FILES)
        else:
            print("请输入正确命令")

main()

