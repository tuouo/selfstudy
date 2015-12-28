#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
a = np.arange(12).reshape(2, 3, 2)
b = np.arange(12, 24).reshape(2,2,3)
print(a)
print(b)
c = np.dot(a,b)
print(c)

a= np.arange(12).reshape(3,4)
print(a, a.dtype)
a.tofile("a.bin")
b = np.fromfile("a.bin", dtype = np.float)
print(b)
b = np.fromfile("a.bin", dtype = np.int32)
print(b)
b.shape = (3,4)
print(b)
