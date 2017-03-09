#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = [[1, 2], [3, 4], [5, 6], [7, 8]]
aa = sum(a, [])
# [1, 2, 3, 4, 5, 6, 7, 8]
print(aa)

b = [[1], [2]]
print(sum(b, [9]))
bb = [[1], [2], [3, 4]]
print(sum(bb, [9]))

c = [1, 2, [3]]
print(c + [])

print([1, 2] + [3, 4])