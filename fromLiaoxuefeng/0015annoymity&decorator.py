#!/usr/bin/env python3
# -*- coding: utf-8 -*-
l = list(map(lambda x: x * x, range(10)))
print(l)
f = lambda x : x * (x - 1)
print(f(3), f)
print(list(map(f, range(10, 100, 10))))
print(f.__name__)		# __name__ not _name_

def build(x, y):
    return lambda: x * x + y * y
print(build(3, 4)())

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log					#log(justPrint)
def justPrint():
    print('OK')
print(justPrint.__name__)
justPrint()

def logMess(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' %(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@logMess('execute')		#logMess('execute')(justPrint2)
def justPrint2():		
    print("OK2")
print(justPrint2.__name__)
justPrint2()

import functools
def log2(func):
    @functools.wraps(func)
    def wrapper2(*args, **kw):
        print('call() %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper2
@log2
def justPrint3():
    print('OK3')
print(justPrint3.__name__)
justPrint3()	

def logMess2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' %(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@logMess2('logMess2-execute')
def justPrint4():
    print('OK4')
print(justPrint4.__name__)
justPrint4()

def logPreNext(*text):
    def decoratorPreNext(func):
        @functools.wraps(func)
        def wrapperPreNext(*args, **kw):
            print('begin call %s():%s ' %(func.__name__, text))
            func(*args, **kw)
            print('end call %s():' % func.__name__)
            return			
        return wrapperPreNext
    return decoratorPreNext
@logPreNext('logMess2-execute')
def justPrintPreNext():
    print('OKPreNext')
print(justPrintPreNext.__name__)
justPrintPreNext()