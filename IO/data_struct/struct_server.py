import struct
from socket import *
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('0.0.0.0',8888)) 
print("Waiting.....")
#确定好数据结果
st = struct.Struct('i5sf')

while True:
    data, addr = s.recvfrom(1024)
    if not data:
        break
    data = st.unpack(data)
    print(data)
s.close()