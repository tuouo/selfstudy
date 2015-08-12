#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def calcSum(*args):
    ax = 0
    for n in args:
        ax += n
    return ax
	
def lazysum(*args):
    def inSum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return inSum
	
f = lazysum(1, 2, 3, 4, 5)
print(f)
print(f())
print(lazysum(1, 2, 3, 4, 5)())
f2 = lazysum(1, 2, 3, 4, 5)
print(f2, f == f2)

def countPow():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = countPow()
print(f1(), f2(), f3())		# do not rely on variable

def countPow1():
    fs = []
    for i in range(1, 4):
        def f(n = i):		# ok, n is sure every time
            return n * n
        fs.append(f)
    return fs

def countPow2():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    fs2 = []
    for i in range(1,4):
        fs.append(f(i))		# ok,
        #print(f(i)(), f(i))
        fs2.append(f(i)())
    print(fs2)
    return fs

f1, f2, f3 = countPow2()
print(f1(), f2(), f3())
