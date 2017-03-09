#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing import Process, Queue
import os, time, random

def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' %value)
        q.put(value)
        time.sleep(random.random())

def read(p):
    print('Process to read: %s' % os.getpid())
    while True:
        value = p.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target = write, args = (q,))	
    pr = Process(target = read, args = (q,))	
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()		# stop read or run forever
	
#	Casue not support fork on windows, all class in main process need
# serialized by pickle. so that child process can take over