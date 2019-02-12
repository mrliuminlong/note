启动：sudo /etc/init.d/mysql start
     - 停止：sudo /etc/init.d/mysql stop
     - 重启：sudo /etc/init.d/mysql restart
     - 查看状态：sudo /etc/init.d/mysql status
    　 命令：mysql -h服务器地址 -u用户名 -p用户密码
      示例：mysql -hlocalhost -uroot -p123456
创建库
create database picture;
创建客户注册表
mysql 有四种类型字段储存二进制文件
　　 TinyBlob 255
    Blob  65K
    MediumBlob  16M
    LongBlob 4G
create table myimg(
  id int primary key auto_increment,
  data mediumblob,
  date datetime
);
