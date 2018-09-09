import smtplib
from email.mime.text import MIMEText

# 第三方SMTP服务
mail_host = "smtp.163.com"
mail_user = "gmy_88886666@163.com"
mail_pass = "gaotengfei1989"
sender = "gmy_88886666@163.com"
receivers = ["mingyang.gao@591hx.com"]
tittle = "以为是个王者，谁知只是青铜"
content = """python 邮件学习"
第一步：导入模块 smtplib,和email.mime.text模块里面的MIMEText方法
第二步：第三方SMTP服务 主要用到mail_host服务器，mail_user账户，mail_pass口令授权码
第三步：设置邮件相关内容，sender发送者，receivers接收者，tittle标题，content邮件内容
第四步：封装发送邮件的函数，定义一个sendemail（）函数，设置邮件头部，发送邮件与异常处理。
        def sendemail():
    message = MIMEText(content, "plain", "utf-8") 内容 格式 编码
    message["From"] = "{}".format(sender)  发件人
    message["To"] = ",".join(receivers)     收件人
    message["Subject"] = tittle              标题
    try:
        smtpobj = smtplib.SMTP_SSL(mail_host, 465)  创建SSL连接
        smtpobj.login(mail_user, mail_pass)          登录验证
        smtpobj.sendmail(sender,receivers,message.as_string())    发送邮件
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)
第五步：调用sendemail（）函数执行发送邮件
全部代码：
import smtplib
from email.mime.text import MIMEText

# 第三方SMTP服务
mail_host = 'smtp.163.com'  # 发件服务器

mail_user = 'gmy_88886666@163.com'  # 用户名

mail_pass = 'gaotengfei1989'  # 口令授权码

sender = 'gmy_88886666@163.com'
receivers = ['mingyang.gao@591hx.com']
content = '这是第3封测试邮件，请注意查收'
title = 'Python发送邮件练习'  # 邮件主题

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


"""


def sendemail():
    message = MIMEText(content, "plain", "utf-8")
    message["From"] ="{}".format(sender)
    message["To"] = "".join(receivers)
    message["Subject"] = tittle
    try:
        smtpobj = smtplib.SMTP_SSL(mail_host, 465)
        smtpobj.login(mail_user, mail_pass)
        smtpobj.sendmail(sender,receivers,message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)


sendemail()
