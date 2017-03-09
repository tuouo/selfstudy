#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def consumer():
    r = ''
    while True:
        print("consumer:")
        n = yield r
        print('n =', n)
        # if not n:
            # return
        print('~~~~~~ Consuming %s ...' % n)
        r = '200 OK\n'

def produce(c):
    c.send(None)				# start generator, must be None
    n = 0
    while n < 5:
        n += 1
        print('###### Producing %s ...' % n)
        r = c.send(n)
        print('Consumer return : %s' % r)
    c.close()
	
c = consumer()
produce(c)
