from socket import *
from select import *
#准备要关注的IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

#添加关注列表
rlist = [s]
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
        else:
            data = r.recv(1024)
            if not data:
                #客户端退出从关注列表移除
                rlist.remove(r)
                r.close()
                continue
            print("Receive from %s:%s"% (r.getpeername(),data.decode()))
            r.send(b'Received!')
            wlist.append(r)
            
    # for w in ws:
    #     w.send(b'Receive your message!')
    #     wlist.remove(w)
    # for x in xs:
    #     x.close()
