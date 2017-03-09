#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time, math, numpy as np
x = [i * 0.001 for i in range(100000)]
start = time.clock()
for i, v in enumerate(x):
    x[i] = math.sin(v)
end = time.clock()
print("math.sin:", end - start)

x = [i * 0.001 for i in range(100000)]
start2 = time.clock()
x = np.array(x)
np.sin(x, x)
end2 = time.clock()
print("numpy.sin:", end2 - start2)
print("math/numpy:", (end - start) / (end2 - start2))

x = [i * 0.001 for i in range(100000)]
start3 = time.clock()
for i, v in enumerate(x):
    x[i] = np.sin(v)
end3 = time.clock()
print("numpy.sin per:", end3 - start3)
print("math/per:", (end - start) / (end3 - start3))