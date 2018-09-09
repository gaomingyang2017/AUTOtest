import requests
import logging
logging.basicConfig(filename='app.log',   #输出路径、文件名
                    level=logging.DEBUG,    #日志级别
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',    #日志格式
                    datefmt='%Y-%m-%d %H:%M:%S')
# 查询业务设备列表接口
url='http://api.dev.huaxuntg.com:8444/weixin/empdevice/getlist'
header={'Content-Type':'application/json','token':'123456'}
param={
  "pageNum": 1,
  "pageSize": 30
}
timeout=3
try:
  r=requests.post(url=url,json=param,headers=header,timeout=float(timeout))
  statu=r.status_code
  response=r.text
  exc=r.raise_for_status()
  print(logging.info(statu),end="")
  print(logging.debug(response))

except timeouterror as e:
  print(logging.error(e))

