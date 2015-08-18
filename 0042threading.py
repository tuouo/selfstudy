#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time, threading

print("123")
def loop():
    print('Thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)
	
print('Thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target = loop, name = 'LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
print('321')