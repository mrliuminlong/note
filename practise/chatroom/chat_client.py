#chat client创建
#code = utf-8
from socket import *
import os, sys

def recv_msg(s):
    while True:
        data, addr = s.recvfrom(1024)
        #服务器发来EXIT表示退出
        if data.decode()=="EXIT":
            sys.exit(0)
        print(data.decode())
#发送消息
def send_msg(s, name ,ADDR):
    while True:
        text = input("消息：")
        #输入＃＃表示退出聊天室
        if text =="##":
            msg = "Q "+name
            s.sendto(msg.encode(),ADDR)
            sys.exit("我已经退出聊天室")
        msg = "C %s %s "%(name,text)
        s.sendto(msg.encode(),ADDR)        
#创建套接字
def main():
    #从命令行输入IP
    if len(sys.argv)<3:
        print("argv is error")
        return
    HOST = sys.argv[1]#认为是IP
    PORT = int(sys.argv[2])#认为是端口
    ADDR = (HOST,PORT)
    #创建套接字
    s = socket(AF_INET, SOCK_DGRAM)
    while True:
        name = input("输入姓名：")
        msg = "L "+name
        #发送给服务器，　＂L　＂是表示位，目的是服务端识别
        s.sendto(msg.encode(),ADDR)
        #等待回应
        data, addr = s.recvfrom(128)
        if data.decode() =="ok":
            print("你已经进入聊天室！")
            break
        else:
            print(data.decode())
    #创建父子进程
    pid = os.fork()
    if pid < 0:
        sys.exit("创建进程失败！")
    #发送消息
    elif pid ==0:
        send_msg(s,name,ADDR)
    #接收到消息
    else:
        recv_msg(s)

main()