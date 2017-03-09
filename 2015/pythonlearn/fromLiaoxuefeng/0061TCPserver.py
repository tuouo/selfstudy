#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket, threading, time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '127.0.0.1'
ip = '0.0.0.0'
s.bind((ip, 9999))		# 1024 special
s.listen(5)
print('wait for connection...')

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s close.' % addr)

while True:
    sock, addr = s.accept()
    t = threading.Thread(target = tcplink, args = (sock, addr))	#every socket need a thread
    t.start()