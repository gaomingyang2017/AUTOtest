import smtplib
from email.mime.text import MIMEText

# 第三方SMTP服务
mail_host = 'smtp.163.com'  # 发件服务器

mail_user = 'gmy_88886666@163.com'  # 用户名

mail_pass = 'gaotengfei1989'  # 口令授权码

sender = 'gmy_88886666@163.com'
receivers = ['gmy_88886666@163.com']
content = ""python 连接数据库   pymysql操作代码如下：""
title = 'python 连接mysql获取数据'  # 邮件主题
# 封装一个发送邮件的函数
def sendEmail():
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)


sendEmail()

