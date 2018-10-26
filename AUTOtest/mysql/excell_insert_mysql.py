# -*-usr/bin/env pytohn-*-
# -*-coding:utf-8-*_
# -*-Author:Mingyang.Gao-*-

import pymysql #支持Python3.0
##读取excel使用(支持03)
import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple
from builtins import int

##打开数据库
# conn=pymysql.connect(host='192.168.0.200',user='root',passwd='123456',db='db_casino',port=3310,charset='utf8')
conn = pymysql.connect(host='localhost', user='root', passwd='root', db='sys', port=3306, charset='utf8')
##打开游标
cur = conn.cursor()

##将excel文件导入mysql中
def importExcelToMysql(path):
    workbook = xlrd.open_workbook(path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    ##遍历行
    for i in range(1, worksheet.nrows):
        row = worksheet.row(i)

        ##初始化数组
        sqlstr = []
        ##遍历列
        for j in range(0, worksheet.ncols):
            ##构造数组
            sqlstr.append(worksheet.cell_value(i, j))

        ##插入数据库
        ##test表结构，赋值
        valuestr = [int(sqlstr[0]), str(sqlstr[1]), str(sqlstr[2]), str(sqlstr[3]), str(sqlstr[4]), str(sqlstr[5]),
                    str(sqlstr[6]), str(sqlstr[7]), str(sqlstr[8]),str(sqlstr[9]),str(sqlstr[10]),str(sqlstr[11]),
                    str(sqlstr[12])]

        ##执行sql语句
        ##test表
        cur.execute(
            "insert into test(ID,NAME,NO,D,E,F,G,H,I,J,K,L,M) " +
            "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", valuestr)

    cur.close()
    conn.commit()
    conn.close()
    # 打印信息
    print("数据导入成功！")

##tb_play_type表
read03path = r"C:\Users\Desktop\excel文件\TEST.xls";

##调用函数
importExcelToMysql(read03path)


#  第一步
# python、mysql的安装这里就不详细述说了，有需要的朋友自行百度
#
# xlrd :  可以使用pip安装也可手动下载源码安装，pip安装：pip install xlrd
#
# pymysql : 可以使用pip安装也可手动下载源码安装， pip安装： pip install xlrd
#

#第二步
import xlrd
import pymysql
from datetime import datetime
from xlrd import xldate_as_tuple

# 第三步 读取数据 excel
data = xlrd.open_workbook("D:/sales_data.xls")   //读取D盘中名为sales_data的excel表格
table_one = data.sheet_by_index(0)                      //根据sheet索引获取sheet的内容
table_two = data.sheet_by_index(1)

#创建数据库连接
db = pymysql.connect("localhost", "root", "gaishi123", "sales_data", use_unicode=True, charset="utf8")

for site in sites:
    # 遍历sheet1
    for nrows_one in range(1, int(table_one.nrows)):
        if table_one.cell_value(nrows_one, 0) == site:
            payday = table_one.cell_value(0, 8)
            date = datetime(*xldate_as_tuple(payday, 0))
            payday = date.strftime('%Y/%m/%d')                                 # 出票日期
            sales = float(table_one.cell_value(nrows_one, 1))                  # 销量
            quantity_ticket = int(table_one.cell_value(nrows_one, 2))          # 票数
            rate_electronic = float(table_one.cell_value(nrows_one, 3))        # 电子直销占比
            sales_thanlastweek = float(table_one.cell_value(nrows_one, 4))     # 销量同比上周
            sales_thanlastyear = float(table_one.cell_value(nrows_one, 5))     # 销量同比去年
            break
    # 遍历sheet2
    for nrows_two in range(1, int(table_two.nrows)):
        if table_one.cell_value(nrows_two, 0) == site:
            session = int(table_two.cell_value(nrows_two, 1))                  # 访问量
            rate_conversion = float(table_two.cell_value(nrows_two, 2))        # 转化率
            rate_paysuccess = float(table_two.cell_value(nrows_two, 3))       # 支付成功率
            session_thanlastweek = float(table_two.cell_value(nrows_two, 4))   # 访问量同比上周
            break
    # 将数据存入数据库
    sql = "insert into sales_data(SITE, PAYDAY, SALES, QUANTITY_TICKET, RATE_ELECTRONIC, SALES_THANLASTWEEK," \
          "SALES_THANLASTYEAR, SESSION, SESSION_THANLASTWEEK, RATE_CONVERSION, RATE_PAYSUCCESS)" \
          " values ('%s','%s', %f, %d, %f, %f, %f, %d, %f, %f, %f)" %\
          (site, payday, sales, quantity_ticket, rate_electronic, sales_thanlastweek, sales_thanlastyear,
           session, session_thanlastweek, rate_conversion, rate_paysuccess)
    try:
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        cursor.execute(sql)
    except Exception as e:
        # 发生错误时回滚
        db.rollback()
        print(str(e))
    else:
        db.commit()  # 事务提交
        print('事务处理成功')

