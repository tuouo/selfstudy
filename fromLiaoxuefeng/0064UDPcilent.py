#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientIP = '127.0.0.1'
for data in [b'haha', b'll', b'mess']:
    s.sendto(data, (clientIP, 9999))
    print(s.recv(1024).decode('utf-8'))
s.close()
