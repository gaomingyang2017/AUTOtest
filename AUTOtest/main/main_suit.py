# -*-usr/bin/env pytohn-*-
# -*-coding:utf-8-*_
# -*-Author:Mingyang.Gao-*-
# 测试套件
import unittest
import time
from testcase.testclass import Api_interface_test
from HTMLTestRunner import HTMLTestRunner
from common.SMTP import mail

suite = unittest.TestSuite()
# 测试用例加载
loader = unittest.TestLoader()
# 把测试用例加载到测试套件中
suite.addTests(loader.loadTestsFromTestCase(Api_interface_test))
# suite.addTests(loader.loadTestsFromTestCase('测试用例类名1'))
# suite.addTests(loader.loadTestsFromTestCase('测试用例类名2'))
# 运行并生成测试报告
now_time = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
print(now_time)
# 定义一个报告存放路径
reportfile = r'C:\Users\ASUS\PycharmProjects\AUTOtest\report\%d-report.html'%int(now_time)
fp = open(reportfile, 'wb')
# 定义测试报告
runner = HTMLTestRunner(
    stream=fp,
    title=u'接口测试报告',
    description=u"用例执行情况")
# 运行测试用例
runner.run(suite)
fp.close()
mail.SendEmail(reportfile)
if __name__='__main__':
    runner.run(suite)
    mail.SendEmail(reportfile)