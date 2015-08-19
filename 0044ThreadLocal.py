#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
local_class = threading.local()

def process_student():
    std = local_class.student
    print("Hello, %s (in %s)" % (std, threading.current_thread().name))

def process_thread(args):
    local_class.student = args
    process_student()
	
t1 = threading.Thread(target = process_thread, args = ('Lily',), name = 'Thread-A')
t2 = threading.Thread(target = process_thread, args = ('Bob',), name = 'Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
