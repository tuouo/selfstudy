#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
x = np.linspace(0, 2 * np.pi, 10)
y = np.sin(x)
print(id(x), x)
print(id(y), y)
z = np.sin(x, x)
print(id(z), id(x) == id(z))

a = np.arange(0, 4)
b = np.arange(1, 5)
print(np.add(a, b))
print(a, b)
print(np.add(a, b, a))
print(a, b)

def triangle_func(c, c0, hc):
    def trifunc(x):
        x = x - int(x)
        if x >= c:
        	r = 0.0
        elif x < c0:
        	r = x / c0 * hc
        else:
            r = (c - x) / (c - c0) * hc
        return r
    return np.frompyfunc(trifunc, 1, 1)

x = np.linspace(0, 2, 100)
y = triangle_func(0.6, 0.4, 1.0)(x).astype(np.float64)
print(y)

x, y = np.ogrid[0:5, 0:5]
print("%s\n%s" % (x, y))
x, y = np.ogrid[0:1:4j, 0:1:3j]
print("%s\n%s" % (x, y))

print(np.add.reduce([1, 2, 3]))
print(np.add.reduce([[1, 2, 3], [4, 5, 6]], axis = 1))
print(np.add.accumulate([1, 2, 3]))
print(np.add.accumulate([[1, 2, 3], [4, 5, 6]], axis = 1))

a = np.array([1, 2, 3, 4])
result = np.add.reduceat(a, indices = [0, 1, 0, 2, 0, 3, 0])
print(result)

print(np.multiply.outer([1,2,3,4,5],[2,3,4]))