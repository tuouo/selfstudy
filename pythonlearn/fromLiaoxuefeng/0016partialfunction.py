#!/usr/bin/env python3
# -*- coding: utf-8 -*-
numStr = '1000'
print(numStr, int(numStr))
print(numStr, int(numStr, base = 8))
print(numStr, int(numStr, 16))
print(numStr, int(numStr, 2))

def int2(x, base = 2):
    return int(x, base)
print(numStr, int2(numStr))

import functools
int4 = functools.partial(int, base = 4)
print(numStr, int4(numStr))
print(numStr, int4(numStr, base = 2))
print(numStr, int4(numStr, base = 10))

max2 = functools.partial(max, 10)
print(max2(2, 5, 8))
