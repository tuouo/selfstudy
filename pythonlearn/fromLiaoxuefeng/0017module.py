#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' This is a test module '
__author__ = 'Tengyang Luo'

import sys
def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello world!")
    elif len(args) == 2:
        print(_private1(args[1]))
    else:
        print(_private2())
		
def _private1(name):
    return 'Hello, %s!' % name
	
def _private2():
    return 'Hello, everyone!'
		
if __name__ == '__main__':
    test()