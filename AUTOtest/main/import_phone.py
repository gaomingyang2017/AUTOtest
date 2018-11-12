# -*-usr/bin/env pytohn-*-
# -*-coding:utf-8-*_
# -*-Author:Mingyang.Gao-*-
import requests
def Contactinfo():
    '''采集资源接口'''
    try:
        for i in range( 4305,4355):
            url = 'http://api.dev.huaxuntg.com:8444/customer/contactinfo/collectSource'
            header = {'Content-Type': 'application/json', 'token': '123456'}
            param = {
                        "contactInfo": "",
                        "contactInfoType": 2,
                        "creatorID": 0,
                        "creator": "系统",
                        "menderID": 0,
                        "mediaID": 26,
                        "lastMediaId": 1,
                        "mediaFlag": 1,
                        "lastMediaFlag": 1,
                        "bannerId": 45,
                        "lastBannerId": 0,
                        "companyID": 1087,
                        "empCode": 116999,
                        "empName": "陈剑",
                        "projectName": "今日头条推广"
                    }
            param["contactInfo"] = str((11100000000 + i))
            r = requests.post(url=url, json=param, headers=header)
            print(r.text)
    except Exception as E:
        print('导入错误')

Contactinfo()