from socket import *
s = socket()
s.connect(('127.0.0.1',8888))

f = open('/home/tarena/aid1811/python_net/practise/file_tran/image.jpg','rb')
# s.send("将发送文件！".encode())
while True:
    data = f.read(1024)
    if not data:
        break
    s.send(data)
# s.send("文件发送完毕！".encode())
f.close()
s.close()