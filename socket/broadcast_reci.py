from socket import *
receive = socket(AF_INET, SOCK_DGRAM)
receive.setsockopt(SOL_SOCKET, SO_BROADCAST,1)
receive.bind(('0.0.0.0',6677))
while True:
    try:
        msg,addr = receive.recvfrom(1024)
        print('广播内容：',msg.decode())
        
    except KeyboardInterrupt:
        print("关闭广播！")
        break
    except Exception as e:
        print(e)
receive.close()