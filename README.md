#!/bin/sh
# tkinter_message
python开发的聊天软件
有个a.ico是图标。别忘记下载哦~。
tom和jack是主文件。两个都可以打开，目的是两个会话。
dmpassword是用户密码加密保存在数据库。
MYSQl是操作数据库。
数据库自己创建，自己改
##############    数据库加密连接   ##########
mysql_ssl_rsa_setup --uid=mysql
vim /etc/my.cnf
ssl-ca=/var/lib/mysql/ca.pem
ssl-cert=/var/lib/mysql/server-cert.pem
ssl-key=/var/lib/mysql/server-key.pem
require_secure_transport = ON
bind-address = 0.0.0.0
systemctl  restart mysqld
ALTER USER 'root'@'%' require ssl;                                        #修改用户只允许ssl连接 
grant all privileges on *.* to 'root'@"%" identified by 'Pwd@123456' require ssl;    #授权时候只允许ssl
FLUSH PRIVILEGES;
show variables like '%ssl%';   #查看是否开启ssl连接
\s                              #看是否是ssl连接
#################################################
登陆的时候输入你的名字和想要聊天人的名字。会自己创建信息，保存信息到数据库。同时保存密码。
双方聊天的时候都要输入对方的名字。
数据库里面会创建两个表格。作用是保存消息和消息读取过程
Start：开始读取消息
Status：连接状态
Exit：退出消息
Clear：清空屏幕上消息
History：消息历史记录
ctrl + d 从数据库删除所有聊天记录
