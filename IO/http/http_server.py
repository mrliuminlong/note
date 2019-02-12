#对客户端请求的响应　respnse
from socket import *
#执行函数,处理客户端请求
def handle(connfd):
    print("Connet from.....",connfd.getpeername())
    request = connfd.recv(4096)# 获取http请求
    request_lines = request.splitlines()#请求按行切割
    for line in request_lines:
        print(line)#打印http请求的每一行
    # data = ''' HTTP/1.1 200 OK
    # Content_Encoding:gzip
    # Content_Type:text/html
    # '''
    #响应行，响应头，响应体
    try:
        f = open('index.html')
    except IOError:
        response = "http/1.1 404 Not found\r\n"
        response += '\r\n'
        response += "===sorry not found page==="
    else:
        response = "http/1.1 200 OK\r\n"
        response += '\r\n'
        response += f.read()
    finally:
        connfd.send(response.encode())

#在主函数中创建套接字
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(('0.0.0.0',8001))
    sockfd.listen(5)
    print("Listen to the port 8001...")
    while True:
        connfd, addr = sockfd.accept()
        #处理客户端请求
        handle(connfd)
        connfd.close()
    # sockfd.close()
main()