import socket
while True:
    sockfd = socket.socket()
    addr = ('176.234.83.139', 8881)
    sockfd.connect(addr)
    myqq_no = input("请输入qq号:").encode()
    sockfd.send(myqq_no)
    data = sockfd.recv(1024)
    myqq_pw = input("请输入qq密码:").encode()
    sockfd.send(myqq_pw)
    data = sockfd.recv(1024)
    data = data.decode()
    if data == '1':
        print('登录成功')
        # break
    else:
        print("账号/ 密码错误")

