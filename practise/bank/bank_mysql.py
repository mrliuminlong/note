import pymysql
def Bank(data):
    host = "localhost" # 服务器地址　
    # port 服务器端口（省略连默认端口）
    user = "root" # 用户名
    password = "123456"# 密码
    dbname = "bank"# 库名
    conn = pymysql.connect(host,user,password,dbname)#connect 函数
    cursor = conn.cursor()#创建游标
    sql = '''select acct_no, acct_name, balance from acct
            where acct_no = %s'''%data
    cursor.execute(sql)#游标执行SQL语句
    result = cursor.fetchall()#打印结果
    for r in result:
        acct_no = r[0]
        acct_name = r[1]
        balance = float(r[2])
        if r[2]:
            balance = float(r[2])
        else:
            balance =0.0
    return balance
        # print(("账号：%-15s 户名：%-15s 余额：%.2f") % (acct_no,acct_name,balance))
    conn.close() 
