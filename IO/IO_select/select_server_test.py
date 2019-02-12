#4.编写一个select服务，监听客户端的连接，客户端发送的内容，以及从终端输入的内容。
#  将客户端发送过来的内容和终端输入的内容全部备份到一个文件里


from socket import *
from select import *
import sys
from time import ctime
#准备要关注的IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)
f = open('mylog','a')# 增加日志

#添加关注列表
rlist = [s, sys.stdin]
wlist = []
xlist = []

while True:
    # 监控IO的发生
    rs, ws, xs = select(rlist, wlist, xlist)
    # 遍历３个列表确定那个IO发生
    for r in rs:
        #如果遍历到s说明s就绪则有客户端发起链接
        if r is s:
            c,addr = r.accept()
            print("Connect from ",addr)
            rlist.append(c)
        #客户端链接套接字就绪，则接受消息
        elif r is sys.stdin:
            data = sys.stdin.readline()
            data = ctime()+' '+data +'\n'
            f.write(data)
            f.flush()
        else:
            data = r.recv(1024)
            if not data:
                #客户端退出从关注列表移除
                rlist.remove(r)
                r.close()
                continue
            # print("Receive from %s:%s"% (r.getpeername(),data.decode()))
            # r.send(b'Receive!')
            data = ctime()+' '+data+'\n'
            f.wrire(data)
            f.flush()
            r.send(b'Add logging')
            
            
            
    # for w in ws:
    #     w.send(b'Add logging!')
    #     wlist.remove(w)
    # for x in xs:
    #     x.close()
