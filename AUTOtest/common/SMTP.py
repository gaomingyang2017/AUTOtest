#-*-usr/bin/env pytohn-*-
#-*-coding:utf-8-*_
#-*-Author:Mingyang.Gao-*-
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
host='smtp.163.com'
user='gmy_88886666@163.com'
passwd='gaotengfei1989'
sender='gmy_88886666@163.com'
recevers=['gmy_88886666@163.com','mingyang.gao@591hx.com']
tittle='主题：接口自动化测试报告'
content='''大家好：
        本邮件为本次接口自动化测试报告！
        附件分别为自动化脚本执行日志和接口测试执行报告。
        请大家注意查收

'''

class mail:
    def SendEmail(report):
        message=MIMEMultipart()
        message['From']=sender
        message['To']=",".join(recevers)
        message['Subject']=Header(tittle,'utf-8')
        att1=MIMEText(open(r'F:\app.log', 'rb').read(), 'base64', 'utf-8')
        att1['Content-Type']='application/octet-stream'
        att1['Content-Disposition']="attachment; filename=app.log"

        att2 = MIMEText(open(report, 'rb').read(), 'base64', 'utf-8')
        att2['Content-Type'] = 'application/octet-stream'
        att2['Content-Disposition'] = "attachment; filename=[file]%s"%(report)

        message.attach(MIMEText(content, 'plain', 'utf-8'))
        message.attach(att1)
        message.attach(att2)

        try:
            for recever in recevers:
                smtpObj = smtplib.SMTP_SSL(host, 465)  # 启用SSL发信, 端口一般是465
                smtpObj.login(user, passwd)  # 登录验证
                smtpObj.sendmail(sender, recever, message.as_string())  # 发送
                print("邮件发送成功")
        except smtplib.SMTPException as e:
            print(e)

