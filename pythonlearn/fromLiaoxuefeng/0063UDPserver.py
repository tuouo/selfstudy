#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket, threading, time
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = '127.0.0.1'
ip = '0.0.0.0'
s.bind((ip, 9999))		# listen needn't
print('Bind UDP on 9999...')

def udplink(data, addr):
    print('Received from %s:%s...' % addr)
    #s.sendto(b'Hello, %s!' + data, addr)  #unspport
    #s.sendto(bytes('Hello, %s!' % data, 'utf-8'), addr)
    s.sendto(('Hello, %s!' % data).encode('utf-8'), addr)

while True:
    data, addr = s.recvfrom(1024)
    t = threading.Thread(target = udplink, args = (data, addr))	#every socket need a thread
    t.start()