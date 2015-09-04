#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket, os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# not support AF_INET6
s.connect(('www.sina.com.cn', 80))		# tuple

s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buffer = []
while True:
    d = s.recv(1024)
    if d :
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8')) 
path = os.path.join(os.path.abspath('.'), 'resource')
with open(os.path.join(path, 'sina.html'), 'wb') as f:
   f.write(html)