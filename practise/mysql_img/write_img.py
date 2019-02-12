import pymysql
import sys

#读取图片文件
#blob最大只能存65K的文件
 
fp = open("/home/tarena/aid1811/python_net/practise/mysql_img/girl.jpg",'rb')
img = fp.read()
fp.close()
# 创建连接
conn = pymysql.connect(host='localhost',
                       user='root',
                       passwd='123456',
                       db='picture')
# 创建游标
cursor = conn.cursor()
#注意使用Binary()函数来指定存储的是二进制
#cursor.execute("INSERT INTO demo_pic_repo SET touxiang_data= %s" % pymysql.Binary(img))
sql="insert into myimg (data) VALUES (%s)"
cursor.execute(sql, img)
 
# 提交，不然无法保存新建或者修改的数据
conn.commit()
 
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
