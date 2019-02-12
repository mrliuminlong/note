'''
2019.01.31
@liu
无可奈何花落去，似曾相识燕归来
http 3.0
'''

from socket import *
import sys
from threading import Thread
from settings import *

#创建与web_frame连接的函数
def connect_frame(request_line):
    s = socket()
    try:
        s.connect(frame_address)#连接webframe
    except Exception as e:
        print("连接webframe失败",e)  
        return  
    s.send(request_line.encode())
    response = s.recv(4096*1024).decode()
    s.close()
    return response

#将httpserver功能封装为类
class HTTPServer(object):
    def __init__(self, address):
        self.address = address
        self.create_socket()
        self.bind(address)
    #创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
    #绑定地址
    def bind(self, address):
        self.ip = address[0]
        self.port = address[1]
        self.sockfd.bind(address)
    #启动服务器
    def serve_forever(self):
        self.sockfd.listen(10)
        print("listening 顺丰　%d"%self.port)
        while True:
            connfd,addr = self.sockfd.accept()
            print("Connecting from 客户地址：",addr)
            handle_client = Thread(target=self.handle,args=(connfd,))
            handle_client.setDaemon(True)
            #启动线程
            handle_client.start()
    #处理客户端请求
    def handle(self,connfd):
        request = connfd.recv(1024)
        print("浏览器请求：",request)
        if not request:
            connfd.close()
            return
        request_lines = request.splitlines()
        #获取请求行
        request_line = request_lines[0].decode('utf-8')
        print("间隔行..........")
        print("浏览器请求行：",request_line)
        #调用connect_frame联系webframe后端,webframe返回值
        response_body = connect_frame(request_line)
        response_headlers = "HTTP/1.1 200 ok\r\n"
        response_headlers +="\r\n"
        #拼接响应体
        response =response_headlers + response_body
        connfd.send(response.encode())
        connfd.close()
       
    

if __name__=="__main__":
    #生成对象启动http服务
    httpd = HTTPServer(ADDR)
    httpd.serve_forever()