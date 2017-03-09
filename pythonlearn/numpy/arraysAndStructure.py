#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

a = np.arange(0, 60, 10).reshape(-1, 1) + np.arange(2, 8)
print(a)
def func(i, j):
    return i * 10 + j + 2
print(np.fromfunction(func, (6, 6)))  # not int
print(a[0, 3:5])
print(a[4:, 4:])
print(a[:, 2])
print(a[2::2, 2::2])

print(a[(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)])
print(a[3:, [0, 2, 4]])

mask = np.array([1, 0, 1, 0, 0, 1], dtype = np.bool)
print(a[mask, 2])
print()


persontype = np.dtype({ # names, formats: not others spell
    'names': ['name', 'age', 'weight'], 
    'formats': ['S32', 'i', 'f']
    })
a = np.array([("Zhang", 31, 63), ("Li", 24, 75.5)], dtype = persontype)
print(a.dtype, a, a.tostring())
print(a[0].dtype, a[0])

b = a["weight"]
print(b)
b[1] = 62
print(a[:]["weight"])

c = a[1]
c["name"] = "Wang"
print(a[1]["name"])

include = np.dtype([('f1', [('f2', np.int16)])])
print(include)
inside = np.dtype([('f0', 'i4'), ('f1', 'f8', (2, 3))])
print(inside)

diction = np.dtype({'surname':('S25', 0), 'age':(np.uint8, 25)})
print(diction)

storeZone = np.arange(3).reshape(-1, 1) + np.arange(3)
skipZone = storeZone[::-2, ::-2]
print(storeZone.strides, skipZone.strides)
print(skipZone)