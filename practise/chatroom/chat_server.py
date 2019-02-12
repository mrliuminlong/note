# chat 服务端
#coding = utf-8
'''
chatroom
socket and fork
@liu
'''
from socket import *
import os,sys

#所有和登录有关的判断
def do_login(s,user,name,addr):
    if (name in user) or name =="管理员":
        s.sendto ("该用户已经存在".encode(), addr)
        return
    s.sendto(b"ok", addr)
    #同时通知其他人
    msg="\n欢迎%s进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    #将用户插入
    user[name] = addr
    print(user)

def do_chat(s, user, name, msg):
    msg = "\n%s说:%s"%(name,msg)
    #循环发送所有人，除了自己
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])
            print(user[i])
def do_quit(s,user,name):
    msg = "\n%s 退出聊天室"%name
    for i in user:
        if i == name:
            s.sendto(b"EXIT",user[i])
        else:
            s.sendto(msg.encode(),user[i])
    #删除该用户
    del user[name]
def do_request(s):
    #存储结构{'zhangsan':('127.0.0.1',9999)}
    ｕser = {}
    while True:
        msg, addr = s.recvfrom(1024)
        msgList = msg.decode().split(" ")
        print("msglist:",msgList)
        #区分请求类别
        if msgList[0]=="L":
            do_login(s, user, msgList[1],addr)
        elif msgList[0]=="C":
            msg = " ".join(msgList[2:])
            print("chat:",msg)
            do_chat(s, user, msgList[1],msg)
        elif msgList[0]=="Q":
            do_quit(s,user,msgList[1])
#创建网络链接
def main():
    ADDR = ('0.0.0.0',8888)
    #创建套接字
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)
    #创建多进程　一个处理客户端请求，另一个发送管理员消息
    pid = os.fork()
    if pid < 0:
        print("Create process failed")
        return
    #子进程发送管理员消息　
    elif pid ==0:
        while True:
            msg = input("管理员消息：")
            msg = "C 管理员 "+msg
            s.sendto(msg.encode(),ADDR)
    #父进程处理客户端请求
    else:
        do_request(s)
main()

