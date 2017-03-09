#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
import array
from functools import partial

s = io.StringIO()
print(s.write('Hello World\n')) # return length
print('This is a test', file=s) # return nothing
print(s.getvalue())
s = io.StringIO('Hello\nWorld\n')
print(s.read(4))
print(s.read())

nums = array.array('i', [1, 2, 3, 4, 5])
print(nums)
with open('data.bin', 'wb') as f:
    f.write(nums)
a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
print(a)
with open('data.bin', 'rb') as f:
    f.readinto(a)
print(a)

RECORD_SIZE = 3
with open('data.bin', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)
