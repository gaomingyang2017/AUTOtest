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
recever='gmy_88886666@163.com'
tittle='主题：带附件的邮件发送测试'
content='测试发送邮件。添加桌面附件文件'
class mail:
    def SendEmail():
        message=MIMEMultipart()
        message['From']=sender
        message['To']=recever
        message['Subject']=Header(tittle,'utf-8')
        # att1=MIMEText(open('app.log', 'rb').read(), 'base64', 'utf-8')
        att1=MIMEText(open(r'C:\Users\ASUS\Desktop\ppp.txt', 'rb').read(), 'base64', 'utf-8')

        att1['Content-Type']='application/octet-stream'
        att1['Content-Disposition']="attachment; filename=C:\\Users\\ASUS\\Desktop\\ppp.txt'"
        message.attach(MIMEText(content, 'plain', 'utf-8'))
        message.attach(att1)
        try:
            smtpObj = smtplib.SMTP_SSL(host, 465)  # 启用SSL发信, 端口一般是465
            smtpObj.login(user, passwd)  # 登录验证
            smtpObj.sendmail(sender, recever, message.as_string())  # 发送
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print(e)
mail.SendEmail()
