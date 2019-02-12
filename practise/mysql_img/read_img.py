import pymysql
import sys

# 创建连接
conn = pymysql.connect(host='localhost',
                       user='root',
                       passwd='123456',
                       db='picture')
# 创建游标
cursor = conn.cursor()
cursor.execute('select data from myimg')
data = cursor.fetchone() #fetchall返回duo个元组
print(data)
cursor.close()
with open ("copy_image.jpg",'wb') as f:
    f.write(data[0])
conn.close()