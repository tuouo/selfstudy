#!/usr/bin/env python3
# -*- coding: utf-8 -*-
list = list(range(4, -33, -3))
print(list)
list2 = [x * x for x in range(11, 23, 2) if x % 3 != 0]
print(list2)
list3 = [a + b for a in 'asd' for b in 'zxc']
print(list3)
import os
list4 = [d for d in os.listdir('.') if len(d) < 7]
print(list4)

d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
list5 = [k + '=' + str(v) for k, v in d.items()]
print(list5)

list6 = ['Hello', 'World', 18, 'Apple', None, 'IBM', 'Apple']
list7 = [s.lower() for s in list6 if isinstance(s, str)]
print(list7)
#######################################################
g = (a + b for a in 'asd' for b in 'zxc')
print(g)
print(next(g))
for n in g:
    print(n, ' ', end = '')
print()

def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        print(b, ' ', end = '')
        a, b, n = b, a + b, n + 1
    return "OK."
print(fib(5))

def fibGen(num):
    n, a, b = 0, 0, 1
    while n < num and n < 100:		# n < 100 --> end
        yield b
        a, b, n = b, a + b, n + 1
    return "OK."
print(fibGen(5))
for b in fibGen(5):
    print(b, ' ', end = '')