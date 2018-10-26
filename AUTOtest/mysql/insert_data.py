# -*-usr/bin/env pytohn-*-
# -*-coding:utf-8-*_
# -*-Author:Mingyang.Gao-*-
import configparser
import pymysql
import random
cf = configparser.ConfigParser()
cf.read(r'C:\Users\ASUS\PycharmProjects\AUTOtest\config\config.py')
db = pymysql.connect(
    host=cf.get('mysqldb', 'host'),
    port=cf.getint('mysqldb', 'port'),
    user=cf.get('mysqldb', 'user'),
    password=cf.get('mysqldb', 'password'),
    db=cf.get('mysqldb', 'db'))
curse = db.cursor()
#创建表
# sql1 = 'create table test1(customerid bigint(20),customername varchar(20),city varchar(10),password varchar(10) )'
# sql3='SELECT * FROM Customer LIMIT 10'
# try:
#     curse.execute(sql3)
#     # db.commit()
#     result=curse.fetchall()
#     for i in result:
#         print(i)
# except:
#     print('error:unable to create table')
sql2='insert into test1 (customerid,customername,city,password) values(%d,%s,%s,%s)'
rs=random.sample(range(20000,30000),1000)
citylist=['深圳','广州','北京','武汉','信阳']
for i in rs:
    curse.execute("insert into test1 (customerid,customername,City,password) values(%d,'%s','%s','%s')"%(i,"高明阳"+str(i),"深圳","123456"))
    db.commit()
curse.close()
db.close()
