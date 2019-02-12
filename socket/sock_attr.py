from socket import *

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)#设置端口立即重用
print(s.getsockopt(SOL_SOCKET, SO_REUSEADDR))#得到socketopt 的值
s.bind(('0.0.0.0',8889))
s.listen(3)
print("waiting......  ")
c,addr = s.accept()
# print(s.type)#套接字类型
# print(s.family)#套接字地址
# print(s.getsockname())#获取套接字绑定地址
# print(s.fileno())#获取套接字的文件描述符（操作系统(I/O)操作用的，对文件分配一个唯一文件描述符，以便区分）

# print(c.getpeername())#获取连接套接字客户端地址
# s.setsockopt(level, option, value)
#设置套接字选项功能 （level 选项级别　SOL_SOCKET） （option 选项类别对应的子选项）（value）
print(s.get)