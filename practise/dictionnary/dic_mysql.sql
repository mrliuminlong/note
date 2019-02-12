启动：sudo /etc/init.d/mysql start
     - 停止：sudo /etc/init.d/mysql stop
     - 重启：sudo /etc/init.d/mysql restart
     - 查看状态：sudo /etc/init.d/mysql status
    　 命令：mysql -h服务器地址 -u用户名 -p用户密码
      示例：mysql -hlocalhost -uroot -p123456
创建库
create database dictionary charset=utf8;
创建客户注册表
create table client_login(
  client_id int primary key auto_increment,
  client_name varchar(32) not null,
  client_code varchar(32) default "000000",
  login_date datetime 
) default charset = utf8;


创建客户查询历史记录表
create table history(
    client_id int primary key auto_increment,
    client_name varchar(32) not null,
    checked_word varchar(32) not null,
    checked_time datetime
)default charset = utf8;


创建字典数据库
create table mydictionary(
    word_id int primary key auto_increment,
    word_name varchar(32) not null,
    word_explain text
)default charset = utf8;



