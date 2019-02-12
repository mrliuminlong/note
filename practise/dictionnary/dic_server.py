#电子字典服务端
'''
网络查单词项目
＠liu
2019-01-21
'''
from socket import *
import os,sys
import pymysql
import time
import signal#处理僵尸进程

#定义全局变量
dict_file = "/home/tarena/aid1811/python_net/practise/dictionnary/dict.txt"

def do_register(c, db, data):
    name = data[1]
    passwd = data[2]
    cursor = db.cursor()
    sql = "select * from client_login where client_name='%s'"%name
    cursor.execute(sql)#执行查询操作
    r = cursor.fetchone()
    if r != None:
        c.send(b"exists")
        return   
    #插入用户
    sql = "insert into client_login(client_name,client_code) values('%s','%s')"%(name,passwd)
    try:
        cursor.execute(sql)#执行插入操作
        db.commit()
        c,send(b"ok")
    except Exception:
        db.rollback()
        c.send(b"fail")

def do_login(c,db,data):
    name = data[1]
    passwd = data[2]
    cursor = db.cursor()
    sql = "select * from client_login where client_name = '%s' and client_code ='%s'"%(name,passwd)
    #查找用户
    cursor.execute(sql)
    r = cursor.fetchone()
    if r == None:
        c.send(b"fail")
    else:
        c.send(b"ok")

def do_qurey(c,db,data):
    name = data[1]
    word = data[2]
    #内部函数可以直接使用外部函数变亮　闭包函数
    def insert_history():
        tm = time.ctime()
        sql = "insert into history (client_name,checked_word,checked_time)\
        values(%s,%s,%s)"%(name,word,tm)
        #插历史纪录 
        try:
            cursor.execute(sql)
            db.commit()
        except Exception:
            db.rollback()
    #使用单词本查找
    try:
        f = open('/home/tarena/aid1811/python_net/practise/dictionnary/dict.txt','r')
    except:
        c.send(b"Fail")
        print("open fail")
        return

    for line in f:
        tmp = line.split(" ")[0]
        if tmp > word:
            c.send(b"fail")
            f.close()
            return
        elif tmp == word:
            c.send(line.encode())
            f.close()
            # insert_history()
            return
    c.send(b"Fail")#到结尾衣没有找到
    f.close()

def do_history(c,db,data):
    name = data[1]
    cursor = db.cursor()
    sql = " select * from history where client_name ='%s'"%name
    cursor.execute(sql)
    r = cursor.fetchall()
    if not r:
        c.send(b"fail")
        return
    else:
        c.send(b"ok")
        time.sleep(0.1)
    for i in r:
        msg = "%s,%s,%s"%(i[1],i[2],i[3])
        c.send(msg.encode())
        time.sleep(0.1)
    c.send(b"##")



def do_request_child(c, db):
    while True:
        data = c.recv(128).decode()
        print(c.getpeername(),":",data)
        data = data.split(" ")
        if (not data) or data[0]=="E":
            c.close()
            sys.exit()
        elif data[0] =="R":#注册
            do_register(c,db,data)
        elif data[0] =="L":#登录
            do_login(c,db,data)
        elif data[0] == "Q":#查单词
            do_qurey(c,db,data)
        elif data[0] == "H":#历史纪录
            do_history(c,db,data)

#创建网络链接
def main():
    ADDR = ('0.0.0.0',8005)
    #创建数据库链接
    #db 是数据库对象
    db = pymysql.connect('localhost','root','123456','dictionary')
    #创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(10)
    print("listening...")
    #处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    while True:
        try:
            c,addr = s.accept()
            print("Connect from...",addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue

        #创建父子进程 子进程处理客户端请求
        pid = os.fork()
        if pid ==0:
            s.close()
            do_request_child(c,db)#子进程函数
            sys.exit(0)#为什么退出
        #父进程继续等待新的连接
        else:
            c.close()
main()