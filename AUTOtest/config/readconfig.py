# -*-usr/bin/env pytohn-*-
# -*-coding:utf-8-*_
# -*-Author:Mingyang.Gao-*-
import configparser
import pymysql
cf=configparser.ConfigParser()
cf.read('config.py')   #  读取配置文件内容
# print(cf.sections())  #列表方式获得配置文件中的所有配置节点
# print(cf.items('mysqldb'))  #列表获取配置节点的所有键值对
# print(cf.get('mysqldb','host'))  #得到section中option的值，返回为string类型
# print(cf.getint('mysqldb','port'))  #得到section中option的值，返回为int类型，
# 还有相应的getboolean()和getfloat() 函数。
#add_section(section)   #添加一个新的section
# set( section, option, value)   #对section中的option进行设置，需要调用write将内容写入配置文件。



db=pymysql.connect(
    host=cf.get('mysqldb','host'),
    port=cf.getint('mysqldb','port'),
    user=cf.get('mysqldb','user'),
    password=cf.get('mysqldb','password'),
    db=cf.get('mysqldb','db'))
curse=db.cursor()
sql='SELECT * FROM test1 '
try:
    curse.execute(sql)
    results=curse.fetchall()
    for i in results:
        print(i)
except:
    print('error:unable to fetch data')
curse.close()
db.close()