'''
创建网络单词查询客户端
＠liu
today is good weather!
2019-01-21
'''
from socket import *
import sys
import getpass


def do_register(s):
    while True:
        name = input("输入姓名：")
        #标准库模块　专门用于输入密码 隐式的输入密码
        passwd = getpass.getpass()
        passwd1 = getpass.getpass("再次输入密码")
        if (" " in name) or (" " in passwd):
            print("用户名或密码不能有空格")
            continue
        elif passwd != passwd1:
            print("两次密码不一致")
            continue
        msg = "R %s %s"%(name,passwd)#拼接消息
        #发送请求
        s.send(msg.encode())
        #等待回复
        data = s.recv(1024)
        if data.decode() == "ok":
            print("注册成功")
            login(s,name)#表示直接进入查词界面
        elif data.decode() == "exists":
            print("用户存在")
            break
        else:
            print("注册失败")
            return

def do_login(s):#登录和查单词
    name = input("用户名：")
    passwd = getpass.getpass()
    msg = "L %s %s"%(name,passwd)
    s.send(msg.encode())#发送服务器验证
    data = s.recv(1024).decode()#服务端反馈
    if data == "ok":
        print("登录成功")
        login(s,name)#二级界面
    else:
        print("登录失败")
        return

def login(s, name):#二级界面函数
    while True:
        print('''
        ==========查询界面=========
        --1.查词　2.历史记录　3.注销
        ''')
        cmd = input("输入选项：")
        if cmd == "1":
            do_query(s,name)#查询
        elif cmd =="2":
            do_history(s,name)#查询历史纪录
        elif cmd == "3":
            return
        else:
            print("请输入正确选项")

def do_history(s,name):
    msg = "H %s"%name
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data =="ok":
        while True:
            data = s.recv(1024).decode()
            if data == "##":
                break
            print(data)
    else:
        print("没有历史纪录")

def do_query(s,name):
    while True:
        word = input("输入单词：")
        if word == "##":
            break
        msg = "Q %s %s"%(name,word)  
        s.send(msg.encode())
        data = s.recv(128).decode()
        # if data == "ok":
        data == s.recv(1024).decode()
        print("单词解释：",data)
        # else:
            # print("没有找到该单词")
#创建网络链接
def main():
    ADDR = ('127.0.0.1',8005)
    s = socket()
    try:
        s.connect(ADDR)
    except Exception as e:
        print(e)
        return
    #进入一级界面
    while True:
        print()
        print("**********欢迎登录*********")
        print("======<英－英电子字典>======")
        print("--1.注册　2.　登录　3.退出--")
        print("============================")
        print()
        cmd = input("输入选项：")
        if cmd == "1":
            do_register(s)#注册
            continue
        elif cmd =="2":
            do_login(s)#登录
        elif cmd == "3":
            s.send(b"E")
            sys.exit()
        else:
            print("输入有误，请输入正确选项")
            sys.stdin.flush()#清楚标准输入　输入是放入标准输入流中　缓冲，有可能造成粘包
            continue
      
    
main()