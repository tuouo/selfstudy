#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientIP = ''
clientIP = '127.0.0.1'
s.connect((clientIP, 9998))
print(s.recv(1024).decode('utf-8'))
for data in [b'haha', b'll', b'mess']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
