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

a = np.array([[1,2,3], [4,5,6]])
b = np.arange(0, 1.0, 0.1)
c = np.sin(b)
np.savez("result.npz", a, b, sin_array = c)
r = np.load("result.npz")
print(r["arr_0"])
print(r["arr_1"])
print(r["sin_array"])

a = np.arange(0, 12, 0.5).reshape(4, -1)
np.savetxt("a.txt", a)
print(np.loadtxt("a.txt"))
np.savetxt("a.txt", a, fmt = "%d", delimiter = ",")
print(np.loadtxt("a.txt", delimiter = ","))

a = np.arange(8)
b = np.add.accumulate(a)
c = a + b
with open("result.npy", "wb") as f:
    np.save(f, a)
    np.save(f, b)
    np.save(f, c)
with open("result.npy", "rb") as f:
    print(np.load(f))
    print(np.load(f))
    print(np.load(f))