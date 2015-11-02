#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# work with 0046distributeWorker.py, communicate with each other 

import random, time, queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

task_queue = queue.Queue()
result_queue = queue.Queue()

class queueManager(BaseManager):
    pass
	
def return_task():
    global task_queue
    return task_queue
	
def return_result():
    global result_queue
    return result_queue

def runit():
    # register to net, for communicate
    # windows doesn't work, erase lambda
    #queueManager.register('get_task_queue', callable = lambda:task_queue)	
    #queueManager.register('get_result_queue', callable = lambda:result_queue)
    queueManager.register('get_task_queue', callable = return_task)
    queueManager.register('get_result_queue', callable = return_result)

    # set passport 5000, authkey 'abc', on windows ,IP needed
    #manager = queueManager(address = ('', 5000), authkey = b'abc')
    manager = queueManager(address = ('127.0.0.1', 5000), authkey = b'abc')
    manager.start()

    task = manager.get_task_queue()					# get queue object
    result = manager.get_result_queue()
    for i in range(10):
        n = random.randint(0, 1000)
        print('Put %s in task' % n)
        task.put(n)									# for message in queue, less is batter 
	
    print('Try get result.')
    for i in range(10):
        r = result.get(timeout = 10)
        print('Result: %s' % r)

    manager.shutdown()
    print('manager stop, exit')
	
if __name__ == '__main__':
    #freeze_support()
    runit()