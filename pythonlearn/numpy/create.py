#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])
print(a, a.dtype, a.shape)
print(b, b.dtype, b.shape)
print(c, c.dtype, c.shape)

c.shape = 4, 3
print(c)
c.shape = 2, -1
print(c)

d = a.reshape((2, 2))
print(d)
print(a)
a[1] = 10
print(d)
print(a)

print(np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]], dtype = np.float))
print(np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]], dtype = np.complex))

f = np.arange(0, 1, 0.1)    #from 0 to 1, step = 0.1
print(f, f.dtype, f.shape)
g = np.linspace(0, 1, 12)   #include 1, total = 12, equal difference
print(g, g.dtype, g.shape)
h = np.logspace(0, 2, 20)   #from 0 to 1, total = 20,  equal ratio
print(h, h.dtype, h.shape)

# frombuffer, fromfile, fromstring
latter = "abcdefgh"
i = np.fromstring(latter, dtype = np.int)    # int32
print(i)
print(np.fromstring(latter, dtype = np.int8)
print(np.fromstring(latter, dtype = np.int16))
print("little endian: 97 + 98 * 256 =", 97 + 98 * 256)
print(np.fromstring(latter, dtype = np.float))

def func(i):
    return i % 4 + 1
print(np.fromfunction(func, (10, )))
def func2(i, j):
    return (i + 1) * (j + 1)
print(np.fromfunction(func2, (9, 9)))