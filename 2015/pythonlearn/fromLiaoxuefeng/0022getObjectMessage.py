#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(type(123), type('123'), type(None))
print(type(abs), type(str))
print(int == type(123))			# isinstance interchange is OK

import types
def function1():
    pass
print(type(function1) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)

print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

print(dir(123))
print('123'.__len__())			# __XXX__ is special
print(len('123'))				# actully call __len__()

class Haha(object):
    def __len__(self):
        return 7				# for len()
hahaha = Haha()
print(len(hahaha))