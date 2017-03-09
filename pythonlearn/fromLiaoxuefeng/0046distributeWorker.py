#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time, sys, queue
from multiprocessing.managers import BaseManager

class queueManager(BaseManager):
    pass

# cause register for get queue, so need name only
queueManager.register('get_task_queue')
queueManager.register('get_result_queue')

server_addr = '127.0.0.1'
print('connecting to server %s ...' % server_addr)
# port, authkey need same
m = queueManager(address = (server_addr, 5000), authkey = b'abc')
m.connect()
task = m.get_task_queue()
result = m.get_result_queue()
for i in range(10):
    try:
        n = task.get(timeout = 1)
        print('run task %d * %d.' % (n,n))
        r = '%d * %d = %d' % (n, n, n * n)		
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty')
print('worker exit')
