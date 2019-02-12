from socket import *
from select import *
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)#设置端口复用
s.bind(('0.0.0.0',8888))
s.listen(5)
print("Listening!")
# 创建poll对象
p = epoll()
#建立查找字典
fdmap = {s.fileno():s}# s.fileno() 文件标识符
#注册关注IO
p.register(s, EPOLLIN|EPOLLERR)
while True:
    events = p.poll()#监控IO
    for fd,event in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()            
            print("Connect from", addr)
            #添加新的关注事件
            p.register(c, EPOLLIN|EPOLLHUP)
            fdmap[c.fileno()] = c
        elif event & EPOLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                #客户端退出取消关注，从字典中删除
                p.unregister(fd)
                fdmap[fd].close
                del fdmap[fd]
            else:
                print("Received:",data.decode())
                fdmap[fd].send(b"Received")
    s.close
        
from select import *
p = epoll()
fdmap = {s.fileno():s}
p.register(s, EPOLLIN|EPOLLERR)
while True:
    events = p.poll()
    for fd, event in events:
        if fd = s.fileno():
            c ,addr = fdmap[fd].accept()
            print("Conneting from ",addr)
            p.register(c, EPOLLIN|EPOLLHUP)
            fdmap[c.fileno()]=c
        elif event & EPOLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd)
                fdmap[fd].close
                del fdmap[fd]
            else:
                print("Received :",data.decode())
                fdmap[fd].send(b"Received!")