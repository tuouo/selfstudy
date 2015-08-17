#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re 
m = re.search('(?<=abc)def', 'abcdef')		#aabcdefdef
print(m.group(0))

class Dict(dict):
	# need start with >>> (space here)
	# than need Expected
	# blank line above will treat as part of pre except
	# when except, ... can instead of message
    '''
	>>> d1 = Dict()						
	>>> d1['x'] = 100
	>>> d1.x
	100
	>>> d1.y = 200						
	>>> d1.y
	200
	>>> d2 = Dict(a = 1, b = 2, c = '3')
	>>> d2.c
	'3'
    >>> d2['empty']						
    Traceback (most recent call last):	
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
	'''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
		
def fact(n):
    '''
	>>> print("In fact....")
	In fact....
	>>> fact(1)
	1
	>>> fact(2)
	2
	>>> fact(3)
	6
	>>> fact(0)
	Traceback (most recent call last):
		...
	ValueError
	'''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)
		
if __name__ == '__main__':
    import doctest
    doctest.testmod()