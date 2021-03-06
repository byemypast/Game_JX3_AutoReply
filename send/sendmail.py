# -*- coding: gbk -*-

import core.settings
from core.debug import *
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
def send(subject,maintext):
	debug("send.sendmail.send : subject "+subject+" maintext: "+maintext)
	try:
		mail_host=core.settings.mail_host
		mail_user=core.settings.mail_user
		mail_pass=core.settings.mail_pass
		sender = mail_user #自己发给自己
		receivers = mail_user 
		message = MIMEText(maintext, 'plain', 'utf-8')
		message['From'] = Header("自己", 'utf-8')
		message['To'] =  Header("自己", 'utf-8')
		message['Subject'] = Header(subject, 'utf-8')
		smtpObj = smtplib.SMTP() 
		smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
		smtpObj.login(mail_user,mail_pass)  
		smtpObj.sendmail(sender, receivers, message.as_string())
		debug ("邮件发送成功")
	except Exception as err:
		debug("邮件发送失败！原因："+str(err))
