#!/usr/bin/env python3
# -*- coding: utf-8 -*-
L = list(range(33))
print(L)
print(L[:])
print(L[:10])
print(L[-10:])
print(L[10:17])

print(L[10:17:2], '\t', L[::5])
print((0,1,2,3,4)[:3], '\t', (0,1,2,3,4)[::2], '\t', (0,1,2,3,4)[::-1])
print('qwerty'[:3], '\t', 'qwerty'[::2], '\t', 'qwerty'[::-2])

for i in L:
    print(i, ' ', end = '')
print()
for i in 'qwerty':
    print(i, ' ', end = '')
print()

it = iter(L)
print(next(it))
print(next(it))
print(next(it))
it = iter('zxcvb')
print(next(it))
print(next(it))
print(next(it))
	
d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
for i in d:
    print(i, ' ', end = '')		#random order per time
for i in d.values():
    print(i, ' ', end = '')
for k, v in d.items():
    print(k, v, ' ', end = '')
print()

from collections import Iterable
print(isinstance('asd', Iterable))

for x, y in [(1,8), (2,5), (3,7)]:
    print(x, y)