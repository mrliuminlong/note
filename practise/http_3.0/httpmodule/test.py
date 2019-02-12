#python的http模块　python2 和python3都有
try:
    from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
except ImportError:
    from http.server import BaseHTTPRequestHandler,HTTPServer



#请求处理类
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.requestline)#请求行
        print(self.request)#套接字
        print(self.headers)#请求头

    def do_POST():
        pass

    def do_PUT():
        pass

address = ('0.0.0.0',8080)
#生成服务器对象
server = HTTPServer(address,RequestHandler)
#启动服务器
server.server_forever()