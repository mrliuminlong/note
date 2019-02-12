# #http server 练习
# from socket import *
# def handle(connfd):
#     print("Connecting from ...", connfd.getpeername())
#     request = connfd.recv(4096)
#     request_lines = request.splitlines()
#     for line in request_lines:
#         print(line)
#     try:
#         f = open('index.html')
#     except IOError:
#         response = "http/1.1 404 Not found\r\n"
#         response +='\r\n'
#         response +='====sorry not found page==='
#     else:
#         response = 'http/1.1 200 ok\r\n'
#         response += '\r\n'
#         response += f.read()
#     finally:
#         connfd.send(response.encode())
# def main():
#     sockfd = socket()
#     sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
#     sockfd.bind(('0.0.0.0',8000))
#     sockfd.listen(5)
#     print("Listenning ...")
#     while True:
#         connfd, addr = sockfd.accept()
#         handle(connfd)
#         connfd.close()
# main()
# L = ['a','b','c','d']
# i = 1
# for item in L:
#     print(i, item)
#     i += 1

# for item in enumerate('abcd'):
#     # print(i, item)
#     # i +=1
#     print(item)

# my_dict = {i: i * i for i in range(10)} 
# my_set = {i * 15 for i in range(10)}
# print(my_dict)
# print(my_set)
# s ="ABCDEFG"
# print(s[::-1])
# s = {0,1,2,3}
# s[4]=4
# s.add(4)
# print(s)
# D = [{"name": "Green","age": 30},{"name": "Bob","age":25}]
# D=[1,2,5,8,6]
# print(sorted(D))
# L = [x for x in [[1,2,3],[4,5,6]]]
# # print(L)
# def mynum(x):
# 	if  x > 0:
# 		print  (x,"是正数")
# 		return x
# 	else:
# 		return  x
# 		print (x,"是负数或者0")

# print(mynum(1))
# for i in range(1,5,2):
# 	print(i)
# 	for j in range(3):
# 		if  j == 2:
# 			break
# # 		print(j)

# def f1():
#     v = 200
#     def f2():
#         v = 300
#         def f3():
#             nonlocal v
#             v = 400
#         f3()
#         print('f2.v= ',v )
#     f2()
#     print('f1.v=',v)
# f1()
# d = [{'age': 16, 'name': 'lili'}, {'age': 18, 'name': 'tom'}, {'age': 20, 'name': 'amy'}]
# d2 = [x  for  x  in  d  if  x['age'] <=18]
# print(d2)

# def getfn():
#     def print_hello():
#         print("hello")
#     return print_hello()
# fn = getfn()
# # print(fn)  
# print_hello()

# def print_squre(row):
#      L = [x for x in range(row)]
#      for x in L:
#         print()
#         for y in L:
#            print(y+x, end='')
#     #     print()
#     # return 
# print(print_squre(6))

# L=[1,2,3,4,5,6]

# for x in L:
#     print(str(x).join('|'),end='')
# L = [1,2,3]
# L.remove(1)
# print(L)
# for x in L:
#     print(x)

# L = [1,2,3,4]
# for x in L:
#     L.remove(x)
#     for y in L:
#         L.remove(y)
#         for z in L:
#             pass
#             print(str(x)+str(y)+str(z))
# s='|'
# for x in L:
#     print(s.join(str(x)),end=' ')


# seq = ("a", "b", "c")# 字符串序列
# list=['1','2','3','4','5']
# L = [1,2,3]
# L1=[]
# for x in L:
#     L1.append(str(x))
# seq = L1
# for x in L1:
#     print(s.join(x))
# 
# for x in range(1,5):
#     for y in range(1,5):
#         print(x,y)
        # for z in range(1,5):
        #     print(x,y,z)


# def f(n):
#     a=1
#     b=1
#     for i in range(n):
#         a=a+b
#         b=a+b
#     print('第n个月兔子对数',b)
# f(10)

# def readfile():
#     with open('test.txt') as f:
#         count = 0
#         while count<10:        
#             data += f.readline()
#             count +=1
#             yield data


# f = readfile()
# while True:
#     try:
#         print (next(f), end=" ")
#     except StopIteration:
#         sys.exit()

# with open('/home/tarena/aid1811/python_net/http/test.txt') as f:
#     count = 0
#     data=''
#     while count<3:
#         data += data
#         data = f.readline()  
#         print(data)      
#         count +=1
#     print(data)

# print(1,2,3,sep='#')
# l = [1,2,3]
# def f(a,b,c):
#     print(a)
#     print(b)

# f(*l)

import Tkinter
top = Tkinter.Tk()
# 进入消息循环
top.mainloop()