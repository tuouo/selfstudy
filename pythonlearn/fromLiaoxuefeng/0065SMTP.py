#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
msg = MIMEText('Hello. sent by python', 'plain', 'utf-8')
# from_addr = input("From: ")
# password = input("Password: ")
# to_addr = input("To: ")
# smtp_sever = input("SMTP server: ")
from_addr = '@163.com'
password = ''
to_addr = '@outlook.com'	#  treat as spam
#  http://mail.163.com/help/help_spam_16.htm?ip=115.193.179.73&hostid=smtp13&time=1441433109'

to_addr = '@163.com'
smtp_sever = 'smtp.163.com'

import smtplib
server = smtplib.SMTP(smtp_sever, 25)
server.set_debuglevel(1)
#server.starttls()
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
