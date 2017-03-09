#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
import smtplib, os

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))	# in case of apperance of chinese

# from_addr = input("From: ")
# password = input("Password: ")
# to_addr = input("To: ")
# smtp_sever = input("SMTP server: ")
from_addr = '@163.com'
password = ''
to_addr = ['@126.com', '@gmail.com', '@outlook.com']
smtp_sever = 'smtp.163.com'

msg = MIMEMultipart()
msg['From'] = _format_addr('Pythoner 骆<%s>' % from_addr)

msg['To'] = ";".join((_format_addr('喵<%s>' % to_addr[0]), _format_addr('骆<%s>' % to_addr[1]),  _format_addr('马各<%s>' % to_addr[2]))) 
msg['Subject'] = Header('From SMTP 附件', 'utf-8').encode()

#msg.attach(MIMEText("send with file...", 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello (html)</h1>' +
    '<p><img src = "cid:0"></p>' + 
    '<p><img src = "cid:1"></p>' + 
    '</body></html>', 'html', 'utf-8'))		# cid:X
	
path = os.path.join(os.path.abspath('.'), 'resource')
with open(os.path.join(path, 'random.jpg'), 'rb') as f:
    mime = MIMEBase('image', 'png', filename = 'random.jpg')
    mime.add_header('Content-Disposition', 'attachment', filename = 'random.jpg')
    mime.add_header('Content_ID', '<0>')
    mime.add_header('X-Attachment-ID', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)
with open(os.path.join(path, '123.bmp'), 'rb') as f:
    mime = MIMEBase('image', 'png', filename = '123.bmp')
    mime.add_header('Content-Disposition', 'attachment', filename = '123.bmp')
    mime.add_header('Content_ID', '<1>')
    mime.add_header('X-Attachment-ID', '1')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

server = smtplib.SMTP(smtp_sever, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()