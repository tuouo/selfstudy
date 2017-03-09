#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

a = np.arange(10)
print(a[:3], a[3], a[4:7], a[7:-1])
print(a[1:-1:2], a[5:1:-2])
b = a[::-1]
b[0] = -1
print(b, a)

a = np.arange(10, 0, -1)
b = a[[3, 3, 2, 7, -1]]
print(a, b)
b[0] = 0    # change together
print(a, b)
a[[0, 1, 2, 3]] = 0, 1, 2, 3
print(a, b) # not change together

c = np.arange(5, 0, -1)
print(c)
e = c[[True, False, True, False, False]]
# boolean list: act as 0 & 1
print(e, e == [4, 5, 4, 5, 5])
d = c[np.array([True, False, True, False, False])]
# boolean array: act as this site is chosen or not
print(d, d == [5, 3])
print(d, d == [5, 2]) # d: [5 3]

d = c[np.array([True, False, True, False])]
print(d, d == [5, 3])
d = -1, -2
print(d, c)    # not change together
c[np.array([True, False, True, False])] = -1, -2
print(c)       # change origin

numbers = np.random.rand(10)
print(numbers)
boolean = numbers > 0.5
print(boolean)  # boolean array not boolean list
bignums = numbers[numbers > 0.5]
print(bignums)