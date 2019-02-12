from socket import *
import struct
s = socket(AF_INET, SOCK_DGRAM)
#确定好数据格式
st = struct.Struct('i5sf')
ADRR = (('127.0.0.1',8888))
while True:
    id = int(input("id"))
    name = input("name:")
    height = float(input("height:"))
    data = st.pack(id,name.encode(),height)
    s.sendto(data,ADRR)