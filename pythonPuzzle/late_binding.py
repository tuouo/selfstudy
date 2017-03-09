#!/usr/bin/env python3
# -*- coding: utf-8 -*-
total = []
for i in range(3):
    print(i, end = "")
    total.append(lambda : i)
print()
print(total)
print([i for i in total])
print([i() for i in total])


total = []
for i in range(3):
    total.append(lambda i = i : i)
print([i() for i in total])


total = []
for i in range(3):
    total.append(i)
print(total)