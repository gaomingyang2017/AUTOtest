import pymysql

# 打开数据库连接
db = pymysql.connect(host='39.108.129.136',
                     port=3306, user='boss',
                     password='13902991520',
                     db='mcrm')

# 使用cursor（）方法创建一个游标对象 cursor
cursor = db.cursor()

# 新建查询语句
sql = 'SELECT * FROM Customer LIMIT 10'
try:
    # 使用execute()方法执行sql查询
    cursor.execute(sql)

    # 获取所有记录列表
    results = cursor.fetchall()
    for i in results:
        print(i)
except:
    print('error:unable to fetch data')
# 关闭数据库连接
db.close()
