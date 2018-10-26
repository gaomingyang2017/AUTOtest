# -*-usr/bin/env pytohn-*-
# -*-coding:utf-8-*_
# -*-Author:Mingyang.Gao-*-
import requests
import logging
import unittest
logging.basicConfig(filename=r'F:\app.log',  # 输出路径、文件名
                    level=logging.DEBUG,  # 日志级别
                    format='%(asctime)s %(filename)s[line:%(lineno)d]- %(levelname)s :%(message)s',  # 日志格式
                    datefmt='%Y-%m-%d %H:%M:%S')  # 时间格式

class Api_interface_test(unittest.TestCase):
    def setUp(self):
        pass

    def test_Querydevicelist(self):
        '''查询设备列表'''
        self.url = 'http://api.dev.huaxuntg.com:8444/weixin/empdevice/getlist'
        self.header = {'Content-Type': 'application/json', 'token': '123456'}
        self.param = {"pageNum": 1,"pageSize": 20,"empCode": 118162,"deviceId": "A100005DC2C293"}
        self.timeout = 3
        try:
            r = requests.post(url=self.url, json=self.param, headers=self.header, timeout=float(self.timeout))
            self.response = r.json()
            self.status = r.status_code
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.raise_for_status(),None)
            logging.info(self.status)
            logging.info(self.response)
            print(r.raise_for_status())
        # except r.raise_for_status() as e:  # 接口自动化测一定要raise 异常，不然失败的用例也在报告中显示pass
        #     # print(logging.error(e))
        #     logging.error(e)
        except Exception as E:
            logging.error(E)

    def test_Querydeviceinfo(self):
        '''查询业务设备详情'''
        self.url = 'http://api.dev.huaxuntg.com:8444/weixin/empdevice/queryinfo/{id}'
        self.header = {'Content-Type': 'application/json', 'token': '123456'}
        self.param = {"id": 929}
        self.timeout = 3
        try:
            r = requests.post(url=self.url, json=self.param, headers=self.header, timeout=float(self.timeout))
            self.response = r.json()
            self.status = r.status_code
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.raise_for_status(),None)
            logging.info(self.status)
            logging.info(self.response)
        except Exception as E:
            logging.error(E)

    def test_Getempwxlist(self):
        '''获取业务微信列表'''
        self.url = 'http://api.dev.huaxuntg.com:8444/weixin/empwxinfo/querywxlist'
        self.header = {'Content-Type': 'application/json', 'token': '123456'}
        self.param = {"pageNum": 1,"pageSize": 20,"empCode": 118162}
        self.timeout = 3
        try:
            r = requests.post(url=self.url, json=self.param, headers=self.header, timeout=float(self.timeout))
            self.response = r.json()
            self.status = r.status_code
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.raise_for_status(),None)
            logging.info(self.status)
            logging.info(self.response)
        except Exception as E:
            logging.error(E)

    def test_Getempworktask(self):
        '''获取员工待办工单任务'''
        self.url = 'http://api.huaxuntg.com/worktask/worktask/queryworktask'
        self.header = {'Content-Type': 'application/json', 'token': '123456'}
        self.param = {"notifierId": "113121","readFlag": "","pageNum": 1,"pageSize": 20,"isExecutor": 2}
        self.timeout = 3
        try:
            r = requests.post(url=self.url, json=self.param, headers=self.header, timeout=float(self.timeout))
            self.response = r.json()
            self.status = r.status_code
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.raise_for_status(),None)
            logging.info(self.status)
            logging.info(self.response)
        except Exception as E:
            logging.error(E)





    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
