#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def foo_add(total = []):
    # When the default value for a function argument is an expression,
    # the expression is evaluated only once, not every time the function is called.  
    total.append("bar")
    return total

def foo_default(total = None):
    if total is None:
        total = []
    total.append("bar")
    return total

if __name__ == '__main__':   

    print(foo_add())   # ['bar']
    print(foo_add())   # ['bar', 'bar']
    print(foo_add())   # ['bar', 'bar', 'bar']

    print(foo_default())
    print(foo_default())
    print(foo_default())