#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))	# in case of apperance of chinese
	
# from_addr = input("From: ")
# password = input("Password: ")
# to_addr = input("To: ")
# smtp_sever = input("SMTP server: ")
from_addr = 'ltytuotuo@gmail.com'
password = ''
to_addr = 'ltytuotuo@163.com'
smtp_sever = 'smtp.gmail.com'
#smtp_sever = 'smtp.163.com'
#smtp_sever = 'smtp-mail.outlook.com'

#msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8')	# if both, html first, then plain
msg = MIMEText('<html><body><h1>Hello (html)</h1>' +
    '<p> send by <a href = "http://www.python.org">Python</a>...</p>' + 
    '</body></html>', 'html', 'utf-8')
	
msg['From'] = _format_addr('Pythoner 骆<%s>' % from_addr)
msg['To'] = _format_addr('Receive<%s>' % to_addr)
msg['Subject'] = Header('From SMTP html outlook', 'utf-8').encode()


server = smtplib.SMTP(smtp_sever, 587)	# gmail 
server.starttls()						# Encrypt SMTP
server.set_debuglevel(1)
server.login(from_addr, password)		# outlook not support SMTP AUTH
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()