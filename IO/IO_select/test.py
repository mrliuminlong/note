
# from io import StringIO
# f = StringIO()
# f.write('hello')
# f.write(" ")
# f.write("world!")
# print(f.getvalue())

# f = StringIO("hello\nHi\nwold!")
# while True:
#     s = f.readline()
#     if s =="":
#         break
#     print(s.strip())
from io import BytesIO
f = BytesIO()
f.write("中国".encode('utf-8'))
print(f.getvalue())
f = BytesIO(b'\xe4\xb8\xad\xe5\x9b\xbd')
print(f.read('utf-8'))