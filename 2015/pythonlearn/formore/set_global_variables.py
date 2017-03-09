#!/usr/bin/env python3
# -*- coding: utf-8 -*-
d = {'a': 1, 'b': 'var2', 'c': [1, 2, 3]}
globals().update(d)
print(a, b, c)
print(globals()["a"], globals()["b"], globals()["c"])