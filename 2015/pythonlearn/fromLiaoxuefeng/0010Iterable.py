#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable	# for
a = []	#{}, 'asd', x for x in range(10)
print(isinstance(a, Iterable))
b = 100
print(isinstance(b, Iterable))

from collections import Iterator	# next()
a = (x for x in range(10))
print(isinstance(a, Iterator))
b = []	#{}, 'asd'
print(isinstance(b, Iterator))
print(isinstance(iter(b), Iterator))