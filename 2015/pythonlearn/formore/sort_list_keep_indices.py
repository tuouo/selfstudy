#!/usr/bin/env python3
# -*- coding: utf-8 -*-
l = [4, 2, 3, 5, 1]
print(list(enumerate(l)))
print(sorted((a, b) for (b, a) in enumerate(l)))
values, indices = zip(*sorted((a, b) for (b, a) in enumerate(l)))
print(values)
print(indices)