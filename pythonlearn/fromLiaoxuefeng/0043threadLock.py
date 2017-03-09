#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time, threading
things = 0

def things_inout(n):
    global things
    things += n
    things -= n
	
def many_thread(n):
    for i in range(1000000):	# in this magnitude, 'things' will wrong
        things_inout(n)
		
lock = threading.Lock()
def many_thread2(n):
    for i in range(1000000):	
        lock.acquire()
        try:
            things_inout(n)
        finally:
            lock.release()		
		
		
#t1 = threading.Thread(target = many_thread, args = (3,))	# (a,)
t1 = threading.Thread(target = many_thread2, args = (3,))
#t2 = threading.Thread(target = many_thread, args = (7,))
t2 = threading.Thread(target = many_thread2, args = (7,))
t1.start()
t2.start()
t1.join()
t2.join()
print(things)

# import threading, multiprocessing
# def loop():
    # x = 0
    # while True:
        # x = x ^ 1
		
# for i in range(multiprocessing.cpu_count()):
    # t = threading.Thread(target = loop)
    # t .start()
	
#	Cause Global Interpreter Lock(GIL) in CPython, 
# python really can't mutiProcess. Only mutiThread